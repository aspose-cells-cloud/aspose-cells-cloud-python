Set_Test_Env -TestEnv $TestEnv        
    Write-Host "Start Aspose.Cells Cloud SDK for Python"
    $StartTime = Get-Date
    $passed = 0
    $total =0
    $failed = 0
    $skipped =0
   
    [string[]] $lines = python .\test\run_test.py  
    foreach ($line in $lines) {
        if($line -match [Regex]::Escape(' ... ok'))
        {
            $passed++
        }
        if($line -match "Ran (\d+) tests"){  
            $total=$matches[1]
        }
    }
    $failed = $total -  $passed
    $EndTime = Get-Date
    $timespan ="{0:N2}" -f (New-TimeSpan $StartTime  $EndTime).TotalSeconds
    Write-Host "Spent ${timespan}s on finishing test. Result : Total ${total}, Passed ${passed} , Failed ${failed} ,Skipped ${skipped} ."
    