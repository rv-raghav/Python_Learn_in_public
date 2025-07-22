chai_type = "Plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "irani"
    kitchen()


front_desk()
print("final global chai:", chai_type)