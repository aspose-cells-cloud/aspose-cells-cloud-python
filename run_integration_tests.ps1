<#
.SYNOPSIS
    Runs the Aspose.Cells Cloud SDK integration tests, tallies the results, and
    generates a test report.

.DESCRIPTION
    This script drives the generated pytest integration suite, captures the
    results as JUnit XML, counts passed / failed / errored / skipped tests, and
    writes a Markdown report (plus the raw JUnit XML) into the report directory.

.PARAMETER ClientId
    Aspose Cloud Client ID. Defaults to the CellsCloudClientId environment
    variable. Without credentials every test is reported as skipped.

.PARAMETER ClientSecret
    Aspose Cloud Client Secret. Defaults to CellsCloudClientSecret.

.PARAMETER BaseUrl
    API base URL. Defaults to CellsCloudApiBaseUrl, then https://api.aspose.cloud.

.PARAMETER TestPath
    pytest target. Defaults to "integration_tests".

.PARAMETER ReportDir
    Directory that receives the report. Defaults to "test_report".

.PARAMETER NoReport
    When supplied, results are printed to the console only and no report files
    are written.

.EXAMPLE
    .\run_integration_tests.ps1

.EXAMPLE
    .\run_integration_tests.ps1 -ClientId "..." -ClientSecret "..."
#>

[CmdletBinding()]
param(
    [string]$ClientId = $env:CellsCloudClientId,
    [string]$ClientSecret = $env:CellsCloudClientSecret,
    [string]$BaseUrl = $env:CellsCloudApiBaseUrl,
    [string]$TestPath = "integration_tests",
    [string]$ReportDir = "test_report",
    [switch]$NoReport
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path

function Write-Step {
    param([string]$Message)
    Write-Host ("[{0}] {1}" -f (Get-Date -Format "HH:mm:ss"), $Message) -ForegroundColor Cyan
}

Write-Step "Aspose.Cells Cloud SDK — integration test runner"

# --- Preflight: locate Python ------------------------------------------- #
$python = $null
foreach ($candidate in @("python", "py")) {
    $found = Get-Command $candidate -ErrorAction SilentlyContinue
    if ($found) { $python = $candidate; break }
}
if (-not $python) {
    Write-Host "ERROR: Python was not found on PATH." -ForegroundColor Red
    exit 1
}
$pythonVersion = & $python -c "import sys; print(sys.version.split()[0])" 2>$null
Write-Step "Using Python $pythonVersion"

# --- Credentials -------------------------------------------------------- #
if (-not $ClientId -or -not $ClientSecret) {
    Write-Host ("WARNING: CellsCloudClientId / CellsCloudClientSecret are not set. " +
        "Integration tests will be reported as skipped.") -ForegroundColor Yellow
}

if (-not $BaseUrl) {
    $BaseUrl = "https://api.aspose.cloud"
}

$env:CellsCloudClientId = $ClientId
$env:CellsCloudClientSecret = $ClientSecret
$env:CellsCloudApiBaseUrl = $BaseUrl

# --- Report directory --------------------------------------------------- #
$junitPath = Join-Path $ReportDir "results.xml"
$reportPath = Join-Path $ReportDir "report.md"
if (-not (Test-Path $ReportDir)) {
    New-Item -ItemType Directory -Path $ReportDir | Out-Null
}

# --- Run pytest --------------------------------------------------------- #
Write-Step "Running pytest against '$TestPath' ..."
Push-Location $root
try {
    & $python -m pytest $TestPath `
        -q `
        --junitxml=$junitPath `
        --tb=short
    $pytestExit = $LASTEXITCODE
}
finally {
    Pop-Location
}
Write-Step ("pytest finished (exit code {0})" -f $pytestExit)

if (-not (Test-Path $junitPath)) {
    Write-Host "ERROR: pytest did not produce a JUnit XML report." -ForegroundColor Red
    exit $pytestExit
}

# --- Parse JUnit XML ---------------------------------------------------- #
[xml]$junit = Get-Content -Path $junitPath -Raw
$cases = @($junit.SelectNodes("//testcase"))
$total = $cases.Count
$failures = 0
$errors = 0
$skipped = 0

$moduleStats = @{}
$failureRows = @()

foreach ($case in $cases) {
    $module = if ($case.classname) { $case.classname } else { "unknown" }
    if (-not $moduleStats.ContainsKey($module)) {
        $moduleStats[$module] = [pscustomobject]@{
            Module = $module
            Tests = 0
            Passed = 0
            Failed = 0
            Errored = 0
            Skipped = 0
            Time = 0.0
        }
    }
    $stat = $moduleStats[$module]
    $stat.Tests += 1
    $stat.Time += [double]$case.time

    $failed = $case.SelectSingleNode("failure")
    $errored = $case.SelectSingleNode("error")
    $skippedNode = $case.SelectSingleNode("skipped")

    if ($failed) {
        $failures += 1
        $stat.Failed += 1
        $failureRows += [pscustomobject]@{
            Module = $module
            Name = $case.name
            Kind = "failure"
            Detail = $failed.message
        }
    }
    elseif ($errored) {
        $errors += 1
        $stat.Errored += 1
        $failureRows += [pscustomobject]@{
            Module = $module
            Name = $case.name
            Kind = "error"
            Detail = $errored.message
        }
    }
    elseif ($skippedNode) {
        $skipped += 1
        $stat.Skipped += 1
    }
    else {
        $stat.Passed += 1
    }
}

$passed = $total - $failures - $errors - $skipped
$passRate = if ($total -gt 0) { [math]::Round(100.0 * $passed / $total, 2) } else { 0 }

# --- Console summary ---------------------------------------------------- #
Write-Host ""
Write-Host "================ TEST SUMMARY ================" -ForegroundColor Green
Write-Host ("Total   : {0}" -f $total)
Write-Host ("Passed  : {0}  ({1}%)" -f $passed, $passRate) -ForegroundColor Green
Write-Host ("Failed  : {0}" -f $failures) -ForegroundColor $(if ($failures) { "Red" } else { "DarkGray" })
Write-Host ("Errors  : {0}" -f $errors) -ForegroundColor $(if ($errors) { "Red" } else { "DarkGray" })
Write-Host ("Skipped : {0}" -f $skipped) -ForegroundColor $(if ($skipped) { "Yellow" } else { "DarkGray" })
Write-Host "=============================================="

if ($NoReport) {
    exit $pytestExit
}

# --- Build Markdown report ---------------------------------------------- #
$lines = New-Object System.Collections.Generic.List[string]
$lines.Add("# Aspose.Cells Cloud SDK — Integration Test Report")
$lines.Add("")
$lines.Add(("- **Generated** : {0}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss")))
$lines.Add(("- **Python**    : {0}" -f $pythonVersion))
$lines.Add(("- **Base URL**  : {0}" -f $BaseUrl))
$lines.Add(("- **Target**    : ``{0}``" -f $TestPath))
$lines.Add("")
$lines.Add("## Summary")
$lines.Add("")
$lines.Add("| Metric | Count |")
$lines.Add("|--------|------:|")
$lines.Add(("| Total   | {0} |" -f $total))
$lines.Add(("| Passed  | {0} |" -f $passed))
$lines.Add(("| Failed  | {0} |" -f $failures))
$lines.Add(("| Errors  | {0} |" -f $errors))
$lines.Add(("| Skipped | {0} |" -f $skipped))
$lines.Add(("| Pass rate | **{0}%** |" -f $passRate))
$lines.Add("")
$lines.Add("## Per-module results")
$lines.Add("")
$lines.Add("| Module | Tests | Passed | Failed | Errors | Skipped | Time (s) |")
$lines.Add("|--------|------:|-------:|-------:|-------:|--------:|---------:|")

foreach ($key in ($moduleStats.Keys | Sort-Object)) {
    $s = $moduleStats[$key]
    $lines.Add(("| {0} | {1} | {2} | {3} | {4} | {5} | {6:F2} |" -f `
        $s.Module, $s.Tests, $s.Passed, $s.Failed, $s.Errored, $s.Skipped, $s.Time))
}
$lines.Add("")

if ($failureRows.Count -gt 0) {
    $lines.Add("## Failures & errors")
    $lines.Add("")
    foreach ($row in $failureRows) {
        $lines.Add(("- **[{0}] {1}::{2}**" -f $row.Kind.ToUpper(), $row.Module, $row.Name))
        $lines.Add("")
        $detail = ($row.Detail -replace "`r?`n", "`n").Trim()
        if ($detail) {
            $lines.Add('```')
            $lines.Add($detail)
            $lines.Add('```')
        }
        $lines.Add("")
    }
}
else {
    $lines.Add("## Failures & errors")
    $lines.Add("")
    $lines.Add("None.")
    $lines.Add("")
}

$lines.Add("## Raw results")
$lines.Add("")
$lines.Add(("Machine-readable JUnit XML: ``{0}``" -f $junitPath))
$lines.Add("")

[System.IO.File]::WriteAllLines($reportPath, $lines, (New-Object System.Text.UTF8Encoding($false)))

Write-Step ("Report written to {0}" -f (Join-Path $ReportDir "report.md"))
Write-Step ("Raw JUnit XML written to {0}" -f $junitPath)

exit $pytestExit
