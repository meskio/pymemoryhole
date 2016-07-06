from zope.interface import implementer

from memoryhole.openpgp import IOpenPGP


@implementer(IOpenPGP)
class Gnupg(object):
    def __init__(self):
        from gnupg import GPG
        self.gpg = GPG()

    def encrypt(self, data, encraddr, signaddr):
        result = self.gpg.encrypt(data, *encraddr, default_key=signaddr)
        self._check_gpg_error(result)
        return result.data

    def decrypt(self, data):
        pass

    def verify(self, data, signature):
        pass

    def _check_gpg_error(self, result):
        stderr = getattr(result, 'stderr', '')
        if getattr(result, 'ok', False) is not True:
            raise RuntimeError('Failed to encrypt/decrypt: %s' % stderr)
