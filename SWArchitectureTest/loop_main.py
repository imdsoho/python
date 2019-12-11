from importlib import reload
import change_module

def main():
    while 1:
        reload(change_module)

        inner = change_module.get_class()
        #inner = change_module.RuntimeChangeDataModule()
        print(id(inner))
        print("---------------")

        input_str = input()

        if input_str == "q":
            break
        else:
            print("[Result] %s" % inner.get_data())

if __name__ == "__main__":
    main()
