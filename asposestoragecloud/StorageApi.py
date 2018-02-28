#!/usr/bin/env python

import sys
import os
import urllib
import json
import re
from models import *
from ApiClient import ApiException


class StorageApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    

    def DeleteFile(self, Path, **kwargs):
        """Remove a specific file. Parameters: path - file path e.g. /file.ext, versionID - file's version, storage - user's storage name.
        Args:
            Path (str):  (required)

            versionId (str):  (optional)

            storage (str):  (optional)

            

        Returns: RemoveFileResponse
        """

        allParams = dict.fromkeys(['Path', 'versionId', 'storage'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method DeleteFile" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in allParams:
                allParams[key] = val
        
        resourcePath = '/storage/file/{path}/?appSid={appSid}&amp;versionId={versionId}&amp;storage={storage}'
        
    
        resourcePath = resourcePath.replace('&amp;','&').replace("/?","?").replace("toFormat={toFormat}","format={format}").replace("{path}","{Path}")

        if 'Path' in allParams and allParams['Path'] is not None:
            resourcePath = resourcePath.replace("{" + "Path" + "}" , str(allParams['Path']))
        else:
            resourcePath = re.sub("[&?]Path.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'versionId' in allParams and allParams['versionId'] is not None:
            resourcePath = resourcePath.replace("{" + "versionId" + "}" , str(allParams['versionId']))
        else:
            resourcePath = re.sub("[&?]versionId.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'storage' in allParams and allParams['storage'] is not None:
            resourcePath = resourcePath.replace("{" + "storage" + "}" , str(allParams['storage']))
        else:
            resourcePath = re.sub("[&?]storage.*?(?=&|\\?|$)", "", resourcePath)
        

        method = 'DELETE'
        queryParams = {}
        headerParams = {}
        formParams = {}
        files = { }
        bodyParam = None

        headerParams['Accept'] = 'application/xml,application/json'
        headerParams['Content-Type'] = 'application/json'

        postData = (formParams if formParams else bodyParam)

        response =  self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams, files=files)

        try:
            if response.status_code in [200,201,202]:
                responseObject = self.apiClient.pre_deserialize(response.content, 'RemoveFileResponse', response.headers['content-type'])
                return responseObject
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

        

        

    def GetDiscUsage(self, **kwargs):
        """Check the disk usage of the current account. Parameters: storage - user's storage name.
        Args:
            storage (str):  (optional)

            

        Returns: DiscUsageResponse
        """

        allParams = dict.fromkeys(['storage'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetDiscUsage" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in allParams:
                allParams[key] = val
        
        resourcePath = '/storage/disc/?appSid={appSid}&amp;storage={storage}'
        
    
        resourcePath = resourcePath.replace('&amp;','&').replace("/?","?").replace("toFormat={toFormat}","format={format}").replace("{path}","{Path}")

        if 'storage' in allParams and allParams['storage'] is not None:
            resourcePath = resourcePath.replace("{" + "storage" + "}" , str(allParams['storage']))
        else:
            resourcePath = re.sub("[&?]storage.*?(?=&|\\?|$)", "", resourcePath)
        

        method = 'GET'
        queryParams = {}
        headerParams = {}
        formParams = {}
        files = { }
        bodyParam = None

        headerParams['Accept'] = 'application/xml,application/json'
        headerParams['Content-Type'] = 'application/json'

        postData = (formParams if formParams else bodyParam)

        response =  self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams, files=files)

        try:
            if response.status_code in [200,201,202]:
                responseObject = self.apiClient.pre_deserialize(response.content, 'DiscUsageResponse', response.headers['content-type'])
                return responseObject
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

        

        

    def GetDownload(self, Path, **kwargs):
        """Download a specific file. Parameters: path - file path e.g. /file.ext, versionID - file's version, storage - user's storage name.
        Args:
            Path (str):  (required)

            versionId (str):  (optional)

            storage (str):  (optional)

            

        Returns: ResponseMessage
        """

        allParams = dict.fromkeys(['Path', 'versionId', 'storage'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetDownload" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in allParams:
                allParams[key] = val
        
        resourcePath = '/storage/file/{path}/?appSid={appSid}&amp;versionId={versionId}&amp;storage={storage}'
        
    
        resourcePath = resourcePath.replace('&amp;','&').replace("/?","?").replace("toFormat={toFormat}","format={format}").replace("{path}","{Path}")

        if 'Path' in allParams and allParams['Path'] is not None:
            resourcePath = resourcePath.replace("{" + "Path" + "}" , str(allParams['Path']))
        else:
            resourcePath = re.sub("[&?]Path.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'versionId' in allParams and allParams['versionId'] is not None:
            resourcePath = resourcePath.replace("{" + "versionId" + "}" , str(allParams['versionId']))
        else:
            resourcePath = re.sub("[&?]versionId.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'storage' in allParams and allParams['storage'] is not None:
            resourcePath = resourcePath.replace("{" + "storage" + "}" , str(allParams['storage']))
        else:
            resourcePath = re.sub("[&?]storage.*?(?=&|\\?|$)", "", resourcePath)
        

        method = 'GET'
        queryParams = {}
        headerParams = {}
        formParams = {}
        files = { }
        bodyParam = None

        headerParams['Accept'] = 'application/xml,application/octet-stream'
        headerParams['Content-Type'] = 'application/json'

        postData = (formParams if formParams else bodyParam)

        response =  self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams, files=files)

        try:
            if response.status_code in [200,201,202]:
                responseObject = self.apiClient.pre_deserialize(response.content, 'ResponseMessage', response.headers['content-type'])
                return responseObject
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

        

        

    def GetIsExist(self, Path, **kwargs):
        """Check if a specific file or folder exists. Parameters: path - file or folder path e.g. /file.ext or /Folder1, versionID - file's version, storage - user's storage name.
        Args:
            Path (str):  (required)

            versionId (str):  (optional)

            storage (str):  (optional)

            

        Returns: FileExistResponse
        """

        allParams = dict.fromkeys(['Path', 'versionId', 'storage'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetIsExist" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in allParams:
                allParams[key] = val
        
        resourcePath = '/storage/exist/{path}/?appSid={appSid}&amp;versionId={versionId}&amp;storage={storage}'
        
    
        resourcePath = resourcePath.replace('&amp;','&').replace("/?","?").replace("toFormat={toFormat}","format={format}").replace("{path}","{Path}")

        if 'Path' in allParams and allParams['Path'] is not None:
            resourcePath = resourcePath.replace("{" + "Path" + "}" , str(allParams['Path']))
        else:
            resourcePath = re.sub("[&?]Path.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'versionId' in allParams and allParams['versionId'] is not None:
            resourcePath = resourcePath.replace("{" + "versionId" + "}" , str(allParams['versionId']))
        else:
            resourcePath = re.sub("[&?]versionId.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'storage' in allParams and allParams['storage'] is not None:
            resourcePath = resourcePath.replace("{" + "storage" + "}" , str(allParams['storage']))
        else:
            resourcePath = re.sub("[&?]storage.*?(?=&|\\?|$)", "", resourcePath)
        

        method = 'GET'
        queryParams = {}
        headerParams = {}
        formParams = {}
        files = { }
        bodyParam = None

        headerParams['Accept'] = 'application/xml,application/json'
        headerParams['Content-Type'] = 'application/json'

        postData = (formParams if formParams else bodyParam)

        response =  self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams, files=files)

        try:
            if response.status_code in [200,201,202]:
                responseObject = self.apiClient.pre_deserialize(response.content, 'FileExistResponse', response.headers['content-type'])
                return responseObject
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

        

        

    def GetListFileVersions(self, Path, **kwargs):
        """Get the file's versions list. Parameters: path - file path e.g. /file.ext or /Folder1/file.ext, storage - user's storage name.
        Args:
            Path (str):  (required)

            storage (str):  (optional)

            

        Returns: FileVersionsResponse
        """

        allParams = dict.fromkeys(['Path', 'storage'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetListFileVersions" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in allParams:
                allParams[key] = val
        
        resourcePath = '/storage/version/{path}/?appSid={appSid}&amp;storage={storage}'
        
    
        resourcePath = resourcePath.replace('&amp;','&').replace("/?","?").replace("toFormat={toFormat}","format={format}").replace("{path}","{Path}")

        if 'Path' in allParams and allParams['Path'] is not None:
            resourcePath = resourcePath.replace("{" + "Path" + "}" , str(allParams['Path']))
        else:
            resourcePath = re.sub("[&?]Path.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'storage' in allParams and allParams['storage'] is not None:
            resourcePath = resourcePath.replace("{" + "storage" + "}" , str(allParams['storage']))
        else:
            resourcePath = re.sub("[&?]storage.*?(?=&|\\?|$)", "", resourcePath)
        

        method = 'GET'
        queryParams = {}
        headerParams = {}
        formParams = {}
        files = { }
        bodyParam = None

        headerParams['Accept'] = 'application/xml,application/json'
        headerParams['Content-Type'] = 'application/json'

        postData = (formParams if formParams else bodyParam)

        response =  self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams, files=files)

        try:
            if response.status_code in [200,201,202]:
                responseObject = self.apiClient.pre_deserialize(response.content, 'FileVersionsResponse', response.headers['content-type'])
                return responseObject
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

        

        

    def PostMoveFile(self, src, dest, **kwargs):
        """Move a specific file.
        Args:
            src (str): source file path e.g. /file.ext (required)

            dest (str):  (required)

            versionId (str): source file's version, (optional)

            storage (str): user's source storage name (optional)

            destStorage (str): user's destination storage name (optional)

            

        Returns: MoveFileResponse
        """

        allParams = dict.fromkeys(['src', 'dest', 'versionId', 'storage', 'destStorage'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method PostMoveFile" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in allParams:
                allParams[key] = val
        
        resourcePath = '/storage/file/{src}/?dest={dest}&amp;appSid={appSid}&amp;versionId={versionId}&amp;storage={storage}&amp;destStorage={destStorage}'
        
    
        resourcePath = resourcePath.replace('&amp;','&').replace("/?","?").replace("toFormat={toFormat}","format={format}").replace("{path}","{Path}")

        if 'src' in allParams and allParams['src'] is not None:
            resourcePath = resourcePath.replace("{" + "src" + "}" , str(allParams['src']))
        else:
            resourcePath = re.sub("[&?]src.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'dest' in allParams and allParams['dest'] is not None:
            resourcePath = resourcePath.replace("{" + "dest" + "}" , str(allParams['dest']))
        else:
            resourcePath = re.sub("[&?]dest.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'versionId' in allParams and allParams['versionId'] is not None:
            resourcePath = resourcePath.replace("{" + "versionId" + "}" , str(allParams['versionId']))
        else:
            resourcePath = re.sub("[&?]versionId.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'storage' in allParams and allParams['storage'] is not None:
            resourcePath = resourcePath.replace("{" + "storage" + "}" , str(allParams['storage']))
        else:
            resourcePath = re.sub("[&?]storage.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'destStorage' in allParams and allParams['destStorage'] is not None:
            resourcePath = resourcePath.replace("{" + "destStorage" + "}" , str(allParams['destStorage']))
        else:
            resourcePath = re.sub("[&?]destStorage.*?(?=&|\\?|$)", "", resourcePath)
        

        method = 'POST'
        queryParams = {}
        headerParams = {}
        formParams = {}
        files = { }
        bodyParam = None

        headerParams['Accept'] = 'application/xml,application/json'
        headerParams['Content-Type'] = 'application/json'

        postData = (formParams if formParams else bodyParam)

        response =  self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams, files=files)

        try:
            if response.status_code in [200,201,202]:
                responseObject = self.apiClient.pre_deserialize(response.content, 'MoveFileResponse', response.headers['content-type'])
                return responseObject
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

        

        

    def PutCopy(self, Path, newdest, file, **kwargs):
        """Copy a specific file. Parameters: path - source file path e.g. /file.ext, versionID - source file's version, storage - user's source storage name, newdest - destination file path, destStorage - user's destination storage name.
        Args:
            Path (str):  (required)

            newdest (str):  (required)

            versionId (str):  (optional)

            storage (str):  (optional)

            destStorage (str):  (optional)

            file (File):  (required)

            

        Returns: ResponseMessage
        """

        allParams = dict.fromkeys(['Path', 'newdest', 'versionId', 'storage', 'destStorage', 'file'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method PutCopy" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in allParams:
                allParams[key] = val
        
        resourcePath = '/storage/file/{path}/?appSid={appSid}&amp;newdest={newdest}&amp;versionId={versionId}&amp;storage={storage}&amp;destStorage={destStorage}'
        
    
        resourcePath = resourcePath.replace('&amp;','&').replace("/?","?").replace("toFormat={toFormat}","format={format}").replace("{path}","{Path}")

        if 'Path' in allParams and allParams['Path'] is not None:
            resourcePath = resourcePath.replace("{" + "Path" + "}" , str(allParams['Path']))
        else:
            resourcePath = re.sub("[&?]Path.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'newdest' in allParams and allParams['newdest'] is not None:
            resourcePath = resourcePath.replace("{" + "newdest" + "}" , str(allParams['newdest']))
        else:
            resourcePath = re.sub("[&?]newdest.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'versionId' in allParams and allParams['versionId'] is not None:
            resourcePath = resourcePath.replace("{" + "versionId" + "}" , str(allParams['versionId']))
        else:
            resourcePath = re.sub("[&?]versionId.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'storage' in allParams and allParams['storage'] is not None:
            resourcePath = resourcePath.replace("{" + "storage" + "}" , str(allParams['storage']))
        else:
            resourcePath = re.sub("[&?]storage.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'destStorage' in allParams and allParams['destStorage'] is not None:
            resourcePath = resourcePath.replace("{" + "destStorage" + "}" , str(allParams['destStorage']))
        else:
            resourcePath = re.sub("[&?]destStorage.*?(?=&|\\?|$)", "", resourcePath)
        

        method = 'PUT'
        queryParams = {}
        headerParams = {}
        formParams = {}
        files = { 'file':open(file, 'rb')}
        bodyParam = None

        headerParams['Accept'] = 'application/xml,application/json'
        headerParams['Content-Type'] = 'multipart/form-data'

        postData = (formParams if formParams else bodyParam)

        response =  self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams, files=files)

        try:
            if response.status_code in [200,201,202]:
                responseObject = self.apiClient.pre_deserialize(response.content, 'ResponseMessage', response.headers['content-type'])
                return responseObject
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

        

        

    def PutCreate(self, Path, file, **kwargs):
        """Upload a specific file. Parameters: path - source file path e.g. /file.ext, versionID - source file's version, storage - user's source storage name, newdest - destination file path, destStorage - user's destination storage name.
        Args:
            Path (str):  (required)

            versionId (str):  (optional)

            storage (str):  (optional)

            file (File):  (required)

            

        Returns: ResponseMessage
        """

        allParams = dict.fromkeys(['Path', 'versionId', 'storage', 'file'])
        allParams['Path'] = Path
        allParams['file'] = file

        resourcePath = '/storage/file/{path}/?appSid={appSid}&amp;versionId={versionId}&amp;storage={storage}'
        
    
        resourcePath = resourcePath.replace('&amp;','&').replace("/?","?").replace("toFormat={toFormat}","format={format}").replace("{path}","{Path}")

        if 'Path' in allParams and allParams['Path'] is not None:
            resourcePath = resourcePath.replace("{" + "Path" + "}" , str(allParams['Path']))
        else:
            resourcePath = re.sub("[&?]Path.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'versionId' in allParams and allParams['versionId'] is not None:
            resourcePath = resourcePath.replace("{" + "versionId" + "}" , str(allParams['versionId']))
        else:
            resourcePath = re.sub("[&?]versionId.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'storage' in allParams and allParams['storage'] is not None:
            resourcePath = resourcePath.replace("{" + "storage" + "}" , str(allParams['storage']))
        else:
            resourcePath = re.sub("[&?]storage.*?(?=&|\\?|$)", "", resourcePath)
        

        method = 'PUT'
        queryParams = {}
        headerParams = {}
        formParams = {}
        files = { 'file':open(file, 'rb')}
        bodyParam = None

        headerParams['Accept'] = 'application/xml,application/json'
        headerParams['Content-Type'] = 'multipart/form-data'

        postData = (formParams if formParams else bodyParam)

        response =  self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams, files=files)

        try:
            if response.status_code in [200,201,202]:
                responseObject = self.apiClient.pre_deserialize(response.content, 'ResponseMessage', response.headers['content-type'])
                return responseObject
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

        

        

    def DeleteFolder(self, Path, **kwargs):
        """Remove a specific folder. Parameters: path - folder path e.g. /Folder1, storage - user's storage name, recursive - is subfolders and files must be deleted for specified path.
        Args:
            Path (str):  (required)

            storage (str):  (optional)

            recursive (bool):  (optional)

            

        Returns: RemoveFolderResponse
        """

        allParams = dict.fromkeys(['Path', 'storage', 'recursive'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method DeleteFolder" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in allParams:
                allParams[key] = val
        
        resourcePath = '/storage/folder/{path}/?appSid={appSid}&amp;storage={storage}&amp;recursive={recursive}'
        
    
        resourcePath = resourcePath.replace('&amp;','&').replace("/?","?").replace("toFormat={toFormat}","format={format}").replace("{path}","{Path}")

        if 'Path' in allParams and allParams['Path'] is not None:
            resourcePath = resourcePath.replace("{" + "Path" + "}" , str(allParams['Path']))
        else:
            resourcePath = re.sub("[&?]Path.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'storage' in allParams and allParams['storage'] is not None:
            resourcePath = resourcePath.replace("{" + "storage" + "}" , str(allParams['storage']))
        else:
            resourcePath = re.sub("[&?]storage.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'recursive' in allParams and allParams['recursive'] is not None:
            resourcePath = resourcePath.replace("{" + "recursive" + "}" , str(allParams['recursive']))
        else:
            resourcePath = re.sub("[&?]recursive.*?(?=&|\\?|$)", "", resourcePath)
        

        method = 'DELETE'
        queryParams = {}
        headerParams = {}
        formParams = {}
        files = { }
        bodyParam = None

        headerParams['Accept'] = 'application/xml,application/json'
        headerParams['Content-Type'] = 'application/json'

        postData = (formParams if formParams else bodyParam)

        response =  self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams, files=files)

        try:
            if response.status_code in [200,201,202]:
                responseObject = self.apiClient.pre_deserialize(response.content, 'RemoveFolderResponse', response.headers['content-type'])
                return responseObject
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

        

        

    def GetListFiles(self, **kwargs):
        """Get the file listing of a specific folder. Parametres: path - start with name of storage e.g. root folder '/'or some folder '/folder1/..', storage - user's storage name.
        Args:
            Path (str):  (optional)

            storage (str):  (optional)

            

        Returns: FilesResponse
        """

        allParams = dict.fromkeys(['Path', 'storage'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetListFiles" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in allParams:
                allParams[key] = val
        
        resourcePath = '/storage/folder/{path}/?appSid={appSid}&amp;storage={storage}'
        
    
        resourcePath = resourcePath.replace('&amp;','&').replace("/?","?").replace("toFormat={toFormat}","format={format}").replace("{path}","{Path}")

        if 'Path' in allParams and allParams['Path'] is not None:
            resourcePath = resourcePath.replace("{" + "Path" + "}" , str(allParams['Path']))
        else:
            resourcePath = re.sub("[&?]Path.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'storage' in allParams and allParams['storage'] is not None:
            resourcePath = resourcePath.replace("{" + "storage" + "}" , str(allParams['storage']))
        else:
            resourcePath = re.sub("[&?]storage.*?(?=&|\\?|$)", "", resourcePath)
        

        method = 'GET'
        queryParams = {}
        headerParams = {}
        formParams = {}
        files = { }
        bodyParam = None

        headerParams['Accept'] = 'application/xml,application/json'
        headerParams['Content-Type'] = 'application/json'

        postData = (formParams if formParams else bodyParam)

        response =  self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams, files=files)

        try:
            if response.status_code in [200,201,202]:
                responseObject = self.apiClient.pre_deserialize(response.content, 'FilesResponse', response.headers['content-type'])
                return responseObject
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

        

        

    def PostMoveFolder(self, src, dest, **kwargs):
        """Move a specific folder. Parameters: src - source folder path e.g. /Folder1, storage - user's source storage name, dest - destination folder path e.g. /Folder2, destStorage - user's destination storage name.
        Args:
            src (str):  (required)

            dest (str):  (required)

            storage (str):  (optional)

            destStorage (str):  (optional)

            

        Returns: MoveFolderResponse
        """

        allParams = dict.fromkeys(['src', 'dest', 'storage', 'destStorage'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method PostMoveFolder" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in allParams:
                allParams[key] = val
        
        resourcePath = '/storage/folder/{src}/?dest={dest}&amp;appSid={appSid}&amp;storage={storage}&amp;destStorage={destStorage}'
        
    
        resourcePath = resourcePath.replace('&amp;','&').replace("/?","?").replace("toFormat={toFormat}","format={format}").replace("{path}","{Path}")

        if 'src' in allParams and allParams['src'] is not None:
            resourcePath = resourcePath.replace("{" + "src" + "}" , str(allParams['src']))
        else:
            resourcePath = re.sub("[&?]src.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'dest' in allParams and allParams['dest'] is not None:
            resourcePath = resourcePath.replace("{" + "dest" + "}" , str(allParams['dest']))
        else:
            resourcePath = re.sub("[&?]dest.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'storage' in allParams and allParams['storage'] is not None:
            resourcePath = resourcePath.replace("{" + "storage" + "}" , str(allParams['storage']))
        else:
            resourcePath = re.sub("[&?]storage.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'destStorage' in allParams and allParams['destStorage'] is not None:
            resourcePath = resourcePath.replace("{" + "destStorage" + "}" , str(allParams['destStorage']))
        else:
            resourcePath = re.sub("[&?]destStorage.*?(?=&|\\?|$)", "", resourcePath)
        

        method = 'POST'
        queryParams = {}
        headerParams = {}
        formParams = {}
        files = { }
        bodyParam = None

        headerParams['Accept'] = 'application/xml,application/json'
        headerParams['Content-Type'] = 'application/json'

        postData = (formParams if formParams else bodyParam)

        response =  self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams, files=files)

        try:
            if response.status_code in [200,201,202]:
                responseObject = self.apiClient.pre_deserialize(response.content, 'MoveFolderResponse', response.headers['content-type'])
                return responseObject
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

        

        

    def PutCopyFolder(self, Path, newdest, **kwargs):
        """Copy a folder. Parameters: path - source folder path e.g. /Folder1, storage - user's source storage name, newdest - destination folder path e.g. /Folder2, destStorage - user's destination storage name.
        Args:
            Path (str):  (required)

            newdest (str):  (required)

            storage (str):  (optional)

            destStorage (str):  (optional)

            

        Returns: ResponseMessage
        """

        allParams = dict.fromkeys(['Path', 'newdest', 'storage', 'destStorage'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method PutCopyFolder" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in allParams:
                allParams[key] = val
        
        resourcePath = '/storage/folder/{path}/?appSid={appSid}&amp;newdest={newdest}&amp;storage={storage}&amp;destStorage={destStorage}'
        
    
        resourcePath = resourcePath.replace('&amp;','&').replace("/?","?").replace("toFormat={toFormat}","format={format}").replace("{path}","{Path}")

        if 'Path' in allParams and allParams['Path'] is not None:
            resourcePath = resourcePath.replace("{" + "Path" + "}" , str(allParams['Path']))
        else:
            resourcePath = re.sub("[&?]Path.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'newdest' in allParams and allParams['newdest'] is not None:
            resourcePath = resourcePath.replace("{" + "newdest" + "}" , str(allParams['newdest']))
        else:
            resourcePath = re.sub("[&?]newdest.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'storage' in allParams and allParams['storage'] is not None:
            resourcePath = resourcePath.replace("{" + "storage" + "}" , str(allParams['storage']))
        else:
            resourcePath = re.sub("[&?]storage.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'destStorage' in allParams and allParams['destStorage'] is not None:
            resourcePath = resourcePath.replace("{" + "destStorage" + "}" , str(allParams['destStorage']))
        else:
            resourcePath = re.sub("[&?]destStorage.*?(?=&|\\?|$)", "", resourcePath)
        

        method = 'PUT'
        queryParams = {}
        headerParams = {}
        formParams = {}
        files = { }
        bodyParam = None

        headerParams['Accept'] = 'application/xml,application/json'
        headerParams['Content-Type'] = 'application/json'

        postData = (formParams if formParams else bodyParam)

        response =  self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams, files=files)

        try:
            if response.status_code in [200,201,202]:
                responseObject = self.apiClient.pre_deserialize(response.content, 'ResponseMessage', response.headers['content-type'])
                return responseObject
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

        

        

    def PutCreateFolder(self, Path, **kwargs):
        """Create the folder. Parameters: path - source folder path e.g. /Folder1, storage - user's source storage name, newdest - destination folder path e.g. /Folder2, destStorage - user's destination storage name.
        Args:
            Path (str):  (required)

            storage (str):  (optional)

            destStorage (str):  (optional)

            

        Returns: ResponseMessage
        """

        allParams = dict.fromkeys(['Path', 'storage', 'destStorage'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method PutCreateFolder" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in allParams:
                allParams[key] = val
        
        resourcePath = '/storage/folder/{path}/?appSid={appSid}&amp;storage={storage}&amp;destStorage={destStorage}'
        
    
        resourcePath = resourcePath.replace('&amp;','&').replace("/?","?").replace("toFormat={toFormat}","format={format}").replace("{path}","{Path}")

        if 'Path' in allParams and allParams['Path'] is not None:
            resourcePath = resourcePath.replace("{" + "Path" + "}" , str(allParams['Path']))
        else:
            resourcePath = re.sub("[&?]Path.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'storage' in allParams and allParams['storage'] is not None:
            resourcePath = resourcePath.replace("{" + "storage" + "}" , str(allParams['storage']))
        else:
            resourcePath = re.sub("[&?]storage.*?(?=&|\\?|$)", "", resourcePath)
        

        if 'destStorage' in allParams and allParams['destStorage'] is not None:
            resourcePath = resourcePath.replace("{" + "destStorage" + "}" , str(allParams['destStorage']))
        else:
            resourcePath = re.sub("[&?]destStorage.*?(?=&|\\?|$)", "", resourcePath)
        

        method = 'PUT'
        queryParams = {}
        headerParams = {}
        formParams = {}
        files = { }
        bodyParam = None

        headerParams['Accept'] = 'application/xml,application/json'
        headerParams['Content-Type'] = 'application/json'

        postData = (formParams if formParams else bodyParam)

        response =  self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams, files=files)

        try:
            if response.status_code in [200,201,202]:
                responseObject = self.apiClient.pre_deserialize(response.content, 'ResponseMessage', response.headers['content-type'])
                return responseObject
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

        

        

    def GetIsStorageExist(self, name, **kwargs):
        """Check if a specific storage exists.
        Args:
            name (str): Storage name (required)

            

        Returns: StorageExistResponse
        """

        allParams = dict.fromkeys(['name'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetIsStorageExist" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in allParams:
                allParams[key] = val
        
        resourcePath = '/storage/{name}/exist/?appSid={appSid}'
        
    
        resourcePath = resourcePath.replace('&amp;','&').replace("/?","?").replace("toFormat={toFormat}","format={format}").replace("{path}","{Path}")

        if 'name' in allParams and allParams['name'] is not None:
            resourcePath = resourcePath.replace("{" + "name" + "}" , str(allParams['name']))
        else:
            resourcePath = re.sub("[&?]name.*?(?=&|\\?|$)", "", resourcePath)
        

        method = 'GET'
        queryParams = {}
        headerParams = {}
        formParams = {}
        files = { }
        bodyParam = None

        headerParams['Accept'] = 'application/xml,application/json'
        headerParams['Content-Type'] = 'application/json'

        postData = (formParams if formParams else bodyParam)

        response =  self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams, files=files)

        try:
            if response.status_code in [200,201,202]:
                responseObject = self.apiClient.pre_deserialize(response.content, 'StorageExistResponse', response.headers['content-type'])
                return responseObject
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

        

        

    




