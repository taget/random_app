from app import version_obj

def test_version_obj():
    ver_obj = version_obj.version_obj('', '1.0')
    ver_obj1 = version_obj.version_obj('', '1.1')
    ver_obj2 = version_obj.version_obj('', '1.2')
    ver_obj3 = version_obj.version_obj('', '0.9')
    print ver_obj1 == ver_obj
    print ver_obj < ver_obj2
    print ver_obj > ver_obj3

    print ver_obj < ver_obj3

test_version_obj()
