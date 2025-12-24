def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "kesar"
    kitchen()
    print(chai_type)

update_order()