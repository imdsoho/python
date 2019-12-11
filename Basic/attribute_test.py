class DynamicAttributes:
    def __init__(self, attr):
        self.attribute = attr

    def __getattr__(self, attr):
        if attr.startswith("fallback_"):
            name = attr.replace("fallback_", "")

            return f"[fallback resolved] {name}"

        raise AttributeError(f"{self.__class__.__name__}에는 {attr} 속성 없음")

dyn = DynamicAttributes("values")
#print(dyn.attribute)

#print(dyn.fallback_test)

#print(dyn.none_attr)
print(getattr(dyn, "something", "default"))

print(dyn.__dict__)

