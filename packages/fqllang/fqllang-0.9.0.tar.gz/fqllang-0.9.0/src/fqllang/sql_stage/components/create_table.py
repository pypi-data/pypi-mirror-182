class CreateTable:
    def __init__(self, name, *fields) -> None:
        self.name = name
        self.fields = fields

    def generate(self):
        result = self.generate_header()
        result += self.generate_body()
        result += self.generate_footer()
        return result

    def generate_header(self):
        return f"create table {self.name}("

    def generate_body(self):
        return ",".join(field.generate() for field in self.fields)

    def generate_footer(self):
        return ");"
    
    def str(self):
        return self.generate()