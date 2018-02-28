#!/usr/bin/env python

import sys
import os
import re
import string
import urllib
import urllib2
import httplib
import json
import datetime
import mimetypes
import random
import string
import hmac
import hashlib
import requests
import httplib
import logging

from models import *
from urlparse import urlparse
from requests.utils import quote


class ApiClient(object):
    def __init__(self, apiKey=None, appSid=None, debug=False, apiServer='http://api.aspose.cloud/v1.1'):
        if apiKey == None:
            raise Exception('You must pass an apiKey when instantiating the '
                            'APIClient')
        if appSid == None:
            raise Exception('You must pass an apiKey when instantiating the '
                            'appSid')
        if apiServer == None:
            raise Exception('You must pass an apiKey when instantiating the '
                            'apiServer')

        self.apiKey = apiKey
        self.apiServer = apiServer
        self.appSid = appSid
        self.cookie = None
        self.defaultHeaders = {}
        self.boundary = 'Somthing'
        self.debug = debug

        if self.debug == True:
            httplib.HTTPConnection.debuglevel = 1
            logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from requests
            logging.getLogger().setLevel(logging.DEBUG)
            requests_log = logging.getLogger("requests.packages.urllib3")
            requests_log.setLevel(logging.DEBUG)
            requests_log.propagate = True

    @property
    def user_agent(self):
        return self.defaultHeaders['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.defaultHeaders['User-Agent'] = value

    def setDefaultHeader(self, headerName, headerValue):
        self.defaultHeaders[headerName] = headerValue

    @staticmethod
    def build_uri(path, qry_data=None):
        """
        URI Builder - Accept path and query string to generate a URI.

        :param path: e.g http://api.aspose.com/v1/testurl
        :param qry_data: a dictionary which holds query string data e.g {'param1': 'value1', 'param2': 'value2'}
        :return: returns a uri with query string e.g http://api.aspose.com/v1/testurl?param1=value1&param2=value2
        """

        del_dict = {}


        if 'file' in qry_data:
            del qry_data['file']
        
        for (key, val) in qry_data.iteritems():
            if(path.find('{' + key.lower() + '}') >= 0):
                path = path.replace('{' + key.lower() + '}', val)
                del_dict[key] = val

        for (key, val) in del_dict.iteritems():
            del qry_data[key]

        path = path.rstrip('/')

        if qry_data:
            return path + '?' + urllib.urlencode(qry_data)
        else:
            return path

    def sign(self, url_to_sign, appSid, apiKey):

        url_to_sign = url_to_sign.replace(" ", "%20");

        url = urlparse(url_to_sign);

        if url.query == "":
            url_part_to_sign = url.scheme + "://" + url.netloc + url.path
        else:
            url_part_to_sign = url.scheme + "://" + url.netloc + url.path + "?" + url.query

        logging.debug("url_part_to_sign" + url_part_to_sign + "apiKey" + apiKey)
        signature = hmac.new(apiKey, url_part_to_sign, hashlib.sha1).digest().encode('base64')[:-1]
        signature = re.sub('[=_-]', '', signature)
        signature = quote(signature, safe='')

        if url.query == "":
            return url.scheme + "://" + url.netloc + url.path + "?signature=" + signature
        else:
            return url.scheme + "://" + url.netloc + url.path + "?" + url.query + "&signature=" + signature



    def callAPI(self, resourcePath, method, queryParams, postData, headerParams=None, files=None):

        resourcePath = resourcePath.replace("{" + "appSid" + "}" , self.appSid)        
        resourcePath = re.sub("\\{\\w*\\}", "", resourcePath)

        url = self.apiServer + resourcePath
        url =    self.sign(url, self.appSid, self.apiKey)
        logging.debug(url)

        mergedHeaderParams = self.defaultHeaders.copy()
        mergedHeaderParams.update(headerParams)
        headers = {}
        if mergedHeaderParams:
            for param, value in mergedHeaderParams.iteritems():
                headers[param] = ApiClient.sanitizeForSerialization(value)

        if self.cookie:
            headers['Cookie'] = ApiClient.sanitizeForSerialization(self.cookie)

        data = None

        if method in ['GET']:
            #Options to add statements later on and for compatibility
            pass

        elif method in ['POST', 'PUT', 'DELETE']:
            if postData:
                postData = ApiClient.sanitizeForSerialization(postData)
                if 'Content-type' not in headers:
                    headers['Content-type'] = 'application/json'
                    data = json.dumps(postData)
                elif headers['Content-type'] == 'multipart/form-data':
                    data = self.buildMultipartFormData(postData, files)

                    headers['Content-type'] = 'multipart/form-data; boundary={0}'.format(self.boundary)
                    headers['Content-length'] = str(len(data))
                else:
                    data = urllib.urlencode(postData)
            elif files:
                headers['Content-type'] = 'multipart/form-data; boundary={0}'.format(self.boundary)
        else:
            raise Exception('Method ' + method + ' is not recognized.')

        if headers['Accept'].find('application/octet-stream') or files:
            stream = True
        else:
            stream = False

        if method == 'GET':
                response = requests.get(url, headers=headers, stream=stream, files=files)
        elif method == 'PUT':
            if 'file' in files and files['file'] and len(files) == 1:
                response = requests.put(url,files['file'], stream=stream)
            else:
                response = requests.put(url,data,headers=headers, stream=stream, files=files)
        elif method == 'POST':
            if 'file' in files and files['file'] and len(files) == 1:
                response = requests.post(url,files['file'], stream=stream)
            else:            
                response = requests.post(url,data,headers=headers, stream=stream, files=files)
        elif method == 'DELETE':
            response = requests.delete(url,data=data,headers=headers, stream=stream, files=files)

        return response


    def toPathValue(self, obj):
        """Convert a string or object to a path-friendly value
        Args:
            obj -- object or string value
        Returns:
            string -- quoted value
        """
        if type(obj) == list:
            return ','.join(obj)
        else:
            return str(obj)

    @staticmethod
    def sanitizeForSerialization(obj):
        """
        Sanitize an object for Request.
        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date convert to string in iso8601 format.
        If obj is list, santize each element in the list.
        If obj is dict, return the dict.
        If obj is swagger model, return the properties dict.
        """
        if isinstance(obj, type(None)):
            return None
        elif isinstance(obj, (str, int, long, float, bool, file)):
            return obj
        elif isinstance(obj, list):
            return [ApiClient.sanitizeForSerialization(subObj) for subObj in obj]
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        else:
            if isinstance(obj, dict):
                objDict = obj
            else:
            # Convert model obj to dict except attributes `swaggerTypes`, `attributeMap`
            # and attributes which value is not None.
            # Convert attribute name to json key in model definition for request.
                objDict = {obj.attributeMap[key]: val
                   for key, val in obj.__dict__.iteritems()
                   if key != 'swaggerTypes' and key != 'attributeMap' and val is not None}
            return {key: ApiClient.sanitizeForSerialization(val)
                 for (key, val) in objDict.iteritems()}

    def buildMultipartFormData(self, postData, files):
        def escape_quotes(s):
            return s.replace('"', '\\"')

        lines = []


        for name, value in postData.items():
            lines.extend((
                '--{0}'.format(self.boundary),
                'Content-Disposition: form-data; name="{0}"'.format(escape_quotes(name)),
                '',
                str(value),
             ))

        for name, filepath in files.items():
            f = open(filepath, 'r')
            filename = filepath.split('/')[-1]
            mimetype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
            lines.extend((
              '--{0}'.format(self.boundary),
              'Content-Disposition: form-data; name="{0}"; filename="{1}"'.format(escape_quotes(name), escape_quotes(filename)),
              'Content-Type: {0}'.format(mimetype),
              '',
              f.read()
            ))

        lines.extend((
          '--{0}--'.format(self.boundary),
          ''
        ))
        return '\r\n'.join(lines)

    def pre_deserialize(self, obj, objClass, contentType=None):
        
        if objClass == 'ResponseMessage':
            if contentType is not None and "application/json" not in contentType:
                objClass = eval('ResponseMessage.ResponseMessage')
                objClass.Status = 'OK'
                objClass.Code = 200
                objClass.InputStream = obj
                return objClass

        if contentType is None or "application/json" not in contentType:
            raise ApiException(406,"Invalid contentType " + str(contentType))
            
        jsonObj = json.loads(obj)
        logging.debug("JSON Body :: " + str(jsonObj))
        return self.deserialize(jsonObj, objClass)

    def deserialize(self, obj, objClass):
        """Derialize a JSON string into an object.
        Args:
            obj -- string or object to be deserialized
            objClass -- class literal for deserialzied object, or string
                of class name
        Returns:
            object -- deserialized object"""

        # Have to accept objClass as string or actual type. Type could be a
        # native Python type, or one of the model classes.
        if obj == None:
            return
         
        if type(objClass) == str:
            if 'list[' in objClass:
                match = re.match('list\[(.*)\]', objClass)
                subClass = match.group(1)
                if obj is not None:
                    return [self.deserialize(subObj, subClass) for subObj in obj]
                else:
                    return;

            if (objClass in ['int', 'float', 'long', 'dict', 'list', 'str', 'bool', 'datetime']):
                objClass = eval(objClass)
            else:  # not a native type, must be model class
                objClass = eval(objClass + '.' + objClass)

        if objClass in [int, long, float, dict, list, str, bool]:
            return objClass(obj)
        elif objClass == datetime:
            return self.__parse_string_to_datetime(obj)

        instance = objClass()

        for attr, attrType in instance.swaggerTypes.iteritems():
            logging.debug(attr + ',' + attrType)
            if obj is not None and instance.attributeMap[attr] in obj and type(obj) in [list, dict]:
                value = obj[instance.attributeMap[attr]]
                if attrType in ['str', 'int', 'long', 'float', 'bool']:
                    attrType = eval(attrType)
                    try:
                        value = attrType(value)
                    except UnicodeEncodeError:
                        value = unicode(value)
                    except TypeError:
                        value = value
                    setattr(instance, attr, value)
                elif (attrType == 'datetime'):
                    setattr(instance, attr, self.__parse_string_to_datetime(value))
                else:
                    setattr(instance, attr, self.deserialize(value, attrType))
            elif obj is not None and instance.attributeMap[attr] not in obj:
                continue
            elif 'list[' in attrType:
                match = re.match('list\[(.*)\]', attrType)
                subClass = match.group(1)
                subValues = []
                if not value:
                    setattr(instance, attr, None)
                else:
                    for subValue in value:
                        subValues.append(self.deserialize(subValue, subClass))
                setattr(instance, attr, subValues)
            else:
                value = obj[instance.attributeMap[attr]]
                setattr(instance, attr, self.deserialize(value, attrType))

        return instance

    def __parse_string_to_datetime(self, string):
        """
        Parse datetime in string to datetime.
        The string should be in iso8601 datetime format.
        """
        try:
            from dateutil.parser import parse
            return parse(string)
        except ImportError:
            return string

class ApiException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def get_code(self):
        return self.code

    def get_message(self):
        return self.message

    def set_code(self, code):
        self.code = code

    def set_message(self, message):
        self.message = message


class MethodRequest(urllib2.Request):
    def __init__(self, *args, **kwargs):
        """Construct a MethodRequest. Usage is the same as for
        `urllib2.Request` except it also takes an optional `method`
        keyword argument. If supplied, `method` will be used instead of
        the default."""

        if 'method' in kwargs:
            self.method = kwargs.pop('method')
        return urllib2.Request.__init__(self, *args, **kwargs)

    def get_method(self):
        return getattr(self, 'method', urllib2.Request.get_method(self))

