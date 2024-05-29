# Decorator method allows you to dynamically add new functionalities to an object without altering its original
# structure by placing the object inside the wrapper object that contains the new functionalities.


class WrittenText:
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text


class BoldText(WrittenText):
    def __init__(self, wrapped_text):
        self.wrapped_text = wrapped_text

    def render(self):
        return f"<b>{self.wrapped_text.render()}</b>"


class ItalicText(WrittenText):
    def __init__(self, wrapped_text):
        self.wrapped_text = wrapped_text

    def render(self):
        return f"<i>{self.wrapped_text.render()}</i>"


class UnderlineText(WrittenText):
    def __init__(self, wrapped_text):
        self.wrapped_text = wrapped_text

    def render(self):
        return f"<u>{self.wrapped_text.render()}</u>"


if __name__ == "__main__":
    input_text = input("Enter text: ")
    before_text = WrittenText(input_text)
    print(before_text.render())

    formatted_text = BoldText(ItalicText(UnderlineText(before_text)))
    print(formatted_text.render())
