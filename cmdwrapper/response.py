import subprocess

class ResponseBase:
    def __init__(self, completed: subprocess.CompletedProcess):
        self._completed = completed
        self.returncode = self._completed.returncode
    
    def check_returncode(self):
        return self._completed.check_returncode()


class PythonVersion(ResponseBase):
    def __init__(self, completed: subprocess.CompletedProcess):
        super().__init__(completed)
        self.check_returncode()
        self.major, self.minor, self.micro, self.qualifier, self.qualifier_version = self._parse(str(completed.stdout, 'utf-8'))

    def _parse(self, stdout: str):
        just_version = stdout.replace('Python', '').strip().split('.')
        assert len(just_version) == 3
        major = int(just_version[0])
        minor = int(just_version[1])
        micro_info = just_version[2]
        micro = None
        qualifier = None
        qualifier_version = None
        qualifier_identifiers = ['a', 'b', 'rc']
        found = False
        for q in qualifier_identifiers:
            if q in micro_info:
                qualifier = q
                micro_info = micro_info.split(q)
                micro = int(micro_info[0])
                qualifier_version = int(micro_info[1])
                found = True
                break
        if not found:
            micro = int(micro_info)
        return major, minor, micro, qualifier, qualifier_version