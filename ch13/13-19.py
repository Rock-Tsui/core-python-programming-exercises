class SortedKeyDict(dict):
    def skeys(self):
        return sorted(self.keys())


if __name__ == '__main__':
    d = SortedKeyDict((('zheng-cai', 67), ('hui-jun', 68), ('xin-yi', 2)))
    print('By iterator:'.ljust(12), [key for key in d])
    print('By keys():'.ljust(12), d.skeys())
