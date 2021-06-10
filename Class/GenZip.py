import zipfile
import random

class genZip:
    def __init__(self, host, port, username, password):
        self.file = 'Class/temp/{0}_proxy_auth_plugin.zip'.format(random.randint(0, 1000000))
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.generate()

    def getManifest(self):
        return """
                {
                    "version": "1.0.0",
                    "manifest_version": 2,
                    "name": "Chrome Proxy",
                    "permissions": [
                        "proxy",
                        "tabs",
                        "unlimitedStorage",
                        "storage",
                        "<all_urls>",
                        "webRequest",
                        "webRequestBlocking"
                    ],
                    "background": {
                        "scripts": ["background.js"]
                    },
                    "minimum_chrome_version":"22.0.0"
                }
                """
    def getBackground(self):
        return """
                        var config = {
                                mode: "fixed_servers",
                                rules: {
                                  singleProxy: {
                                    scheme: "http",
                                    host: "%s",
                                    port: parseInt(%s)
                                  },
                                  bypassList: ["localhost"]
                                }
                              };

                        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

                        function callbackFn(details) {
                            return {
                                authCredentials: {
                                    username: "%s",
                                    password: "%s"
                                }
                            };
                        }

                        chrome.webRequest.onAuthRequired.addListener(
                                    callbackFn,
                                    {urls: ["<all_urls>"]},
                                    ['blocking']
                        );
                        """ % (self.host, self.port, self.username, self.password)
    def generate(self):
        with zipfile.ZipFile(self.file, 'w') as zp:
            zp.writestr("manifest.json", self.getManifest())
            zp.writestr("background.js", self.getBackground())