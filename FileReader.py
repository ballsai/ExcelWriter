import re

class FileReader:

    def __init__(self, path):
        self.path = path
        self.text = []
        self.req_file = False
        self.hostname = ''
        self.model = ''
        self.serial = ''
        self.version = ''

    def readFile(self):
        try: 
            with open(self.path, 'r', errors='ignore') as f_in:
                self.text = list(filter(None, (line.rstrip() for line in f_in)))
        except IOError:
            print('cannot open', self.path)
    
    def isRequired(self, factor):
        if factor:
            self.req_file = True
        return self.req_file
    
    def requiredHostname(self):
        substring = '(#show clock|#enable)' 
        for line in self.text:
            if re.search(substring, line):
                self.hostname = re.sub(substring, '', line)
                break
        return self.hostname

    def requiredModel(self):
        substring = '.*(M|m)odel (N|n)umber.*:'
        for line in self.text:
            if re.search(substring, line):
                self.model = re.sub(substring, '', line)
                break
        return self.model

    def requiredSerial(self):
        substring = '(System (S|s)erial (N|n)umber|Chassis (S|s)erial (N|n)umber).*:'
        for line in self.text:
            if re.search(substring, line):
                self.serial = re.sub(substring, '', line)
                break
        return self.serial
    
    def requiredVersion(self):
        substring = '(Cisco)* IOS.*Software.*Version'
        for line in self.text:
            if re.search(substring, line):
                self.version = re.sub(substring, '', line)
                self.version = re.sub(',| RE\w+', '', self.version)
                break
        return self.version

    def requiredInterfaceDescription(self):
        substring = '.*#show interface description'
        interfaces = '(Interface|Fa|Gi|Po|Vl|Te).*'
        interface_description = []
        modify_interface_description = []
        read_section = False
        
        for line in self.text:
            if re.search(substring, line):
                read_section = True
                continue
            elif read_section:
                if re.search(interfaces, line): 
                    interface_description.append(line)
                else:
                    read_section = False
                    break
        
        for element in interface_description:
            modify_interface_description.append(re.split(r'\s{2,}', element))

        return modify_interface_description
    
    def requiredInterfaceStatus(self):
        substring = '.*#show interface status'
        interfaces = '(Interface|Fa|Gi|Po|Vl|Te).*'
        separator = '\s{2,}.*(connected|notconnect|disabled)'
        replace = ''
        interface_status = []
        modify_interface_status = []
        test = []
        read_section = False

        for line in self.text:
            if re.search(substring, line):
                read_section = True
                continue
            elif read_section:
                if re.search(interfaces, line): 
                    interface_status.append(line)
                else:
                    read_section = False
                    break
        
        for element in interface_status:
            modify_interface_status.append(re.split(r'\s{1,}', re.sub(separator, replace, element)))
        
        return modify_interface_status
    