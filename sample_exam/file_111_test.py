from file_111 import File

def main():

    # Display available permissions
    print('File permissions: {}'.format(File.FILE_PERMISSIONS))

    # Create some files
    f1 = File('poem.txt', 'joe')
    f2 = File('readme.txt', 'max', 1000, 'r')
    f3 = File('secret.txt', 'fred', 100)

    # Display file details
    print('File details...')
    print(f1)
    print(f2)
    print(f3)

    # Check access rights
    print('Access rights...')
    print(f3.has_access('fred', 'r'))
    print(f3.has_access('fred', 'w'))
    print(f3.has_access('fred', 'x'))
    print(f3.has_access('mary', 'r'))
    print(f3.has_access('mary', 'w'))
    print(f3.has_access('mary', 'x'))

    # Fred enables read permission
    print('Fred enables read permission...')
    f3.enable_permission('fred', 'r')

    # Mary enables write permission
    print('Mary enables write permission...')
    f3.enable_permission('mary', 'w')    

    # Check access rights
    print('Access rights...')    
    print(f3.has_access('mary', 'r'))
    print(f3.has_access('mary', 'w'))
    print(f3.has_access('mary', 'x'))
    # Fred enables write and execute permissions
    print('Fred enables write permission...')    
    f3.enable_permission('fred', 'w')
    print('Fred enables execute permission...')    
    f3.enable_permission('fred', 'x')

    # Check access rights
    print('Access rights...')    
    print(f3.has_access('mary', 'r'))
    print(f3.has_access('mary', 'w'))
    print(f3.has_access('mary', 'x'))
    print(f3.has_access('lily', 'r'))
    print(f3.has_access('vera', 'w'))
    print(f3.has_access('bran', 'x'))

#    # Display permissions
    print('Permissions: {}'.format(f3.get_permissions()))

    # Fred disables write permission
    print('Fred disables write permission...')
    f3.disable_permission('fred', 'w')

    # Vera disables execute permission
    print('Vera disables execute permission...')
    f3.disable_permission('vera', 'x')

    # Check access rights
    print('Access rights...')    
    print(f3.has_access('mary', 'r'))
    print(f3.has_access('mary', 'w'))
    print(f3.has_access('mary', 'x'))

    # Display permissions
    print('Permissions: {}'.format(f3.get_permissions()))

    # Play with permissions
    print('Fred disables write permission...')
    f3.disable_permission('fred', 'w')
    print('Permissions: {}'.format(f3.get_permissions()))
    print('Fred enables write permission...')
    f3.enable_permission('fred', 'w')
    print('Fred enables write permission...')
    f3.enable_permission('fred', 'w')
    print('Permissions: {}'.format(f3.get_permissions()))
    f3.enable_permission('fred', 'w')
    print('Fred enables invalid permission...')
    f3.enable_permission('fred', 'z')
    print('Permissions: {}'.format(f3.get_permissions()))

if __name__ == '__main__':
    main()