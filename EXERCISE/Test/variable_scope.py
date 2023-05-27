name = "Brijesh"


def cng_name():
    global name
    name = "Sherbin"
    # print(name)

    def nested():
        # nonlocal name
        name = "Gokul"
        print("1" + name)

    nested()
    print("2" + name)


cng_name()
print("Global : " + name)
