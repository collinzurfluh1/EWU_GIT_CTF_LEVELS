#!/usr/bin/env python3

import base64

def print_something_cool():
    something_cool = b'CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgXy4tIi0uXwogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBfLi0iLS5fJyAgICAgICBgLS5fCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBfLi0iLS5fJyAgICAgICBgLS5fICAgICBfLi0nfAogICAgICAgICAgICAgICAgICAgICAgICAgICAgIF8uLSItLl8nICAgICAgIGAtLl8gICAgIF8uLXxfLi0nXy4tJ2AtLl8KICAgICAgICAgICAgICAgICAgICAgXy4tIi0uXycgICAgICAgYC0uXyAgICAgXy4tfF8uLScgICB8Xy4tJyAgICAgICAgYC0uXwogICAgICAgICAgICAgXy4tIi0uXycgICAgICAgYC0uXyAgICAgXy4tfF8uLScgICAgICAgICAgIGAtLl8gICAgICAgICBfLi18CiAgICAgXy4tIi0uXycgICAgICAgYC0uXyAgICAgXy4tfF8uLScgICAgICAgICAgICAgICAgICAgICAgIGAtLl8gXy4tJ18uLWAtLl8KIF8uLScgICAgICAgYF8uLSItLl8gXy4tfF8uLScgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHxfLi0nICAgICAgIGAtLl8KYC0uXyAgICAgXy4tJyAgICAgICBgXy4tJy0uXyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHwtLl8gICAgICAgICBfLi0nCiAgICBgLS5ffC0uXyAgICAgXy4tJyAgICAgICBgXy4tJy0uXyAgICAgICAgICAgICAgICAgICAgICAgICBfLi0nLS5fYC0uXyBfLi0nCiAgICAgICAgICAgIGAtLl98LS5fICAgICBfLi0nICAgICAgIGBfLi0nLS5fICAgICAgICAgICAgIF8uLScgICAgICAgYC0uX3wKICAgICAgICAgICAgICAgICAgICBgLS5ffC0uXyAgICAgXy4tJyAgICAgICBgXy4tJy0uXyAgICB8LS5fICAgICAgICAgXy4tJwogICAgICAgICAgICAgICAgICAgICAgICAgICAgYC0uX3wtLl8gICAgIF8uLScgICAgICAgYF8uLSctLl9gLS5fIF8uLScKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYC0uX3wtLl8gICAgIF8uLScgICAgICAgYC0uX3wKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBgLS5ffC0uXyAgICAgICAgIF8uLScKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGAtLl8gXy4tJyAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIgo=CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgXy4tIi0uXwogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBfLi0iLS5fJyAgICAgICBgLS5fCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBfLi0iLS5fJyAgICAgICBgLS5fICAgICBfLi0nfAogICAgICAgICAgICAgICAgICAgICAgICAgICAgIF8uLSItLl8nICAgICAgIGAtLl8gICAgIF8uLXxfLi0nXy4tJ2AtLl8KICAgICAgICAgICAgICAgICAgICAgXy4tIi0uXycgICAgICAgYC0uXyAgICAgXy4tfF8uLScgICB8Xy4tJyAgICAgICAgYC0uXwogICAgICAgICAgICAgXy4tIi0uXycgICAgICAgYC0uXyAgICAgXy4tfF8uLScgICAgICAgICAgIGAtLl8gICAgICAgICBfLi18CiAgICAgXy4tIi0uXycgICAgICAgYC0uXyAgICAgXy4tfF8uLScgICAgICAgICAgICAgICAgICAgICAgIGAtLl8gXy4tJ18uLWAtLl8KIF8uLScgICAgICAgYF8uLSItLl8gXy4tfF8uLScgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHxfLi0nICAgICAgIGAtLl8KYC0uXyAgICAgXy4tJyAgICAgICBgXy4tJy0uXyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHwtLl8gICAgICAgICBfLi0nCiAgICBgLS5ffC0uXyAgICAgXy4tJyAgICAgICBgXy4tJy0uXyAgICAgICAgICAgICAgICAgICAgICAgICBfLi0nLS5fYC0uXyBfLi0nCiAgICAgICAgICAgIGAtLl98LS5fICAgICBfLi0nICAgICAgIGBfLi0nLS5fICAgICAgICAgICAgIF8uLScgICAgICAgYC0uX3wKICAgICAgICAgICAgICAgICAgICBgLS5ffC0uXyAgICAgXy4tJyAgICAgICBgXy4tJy0uXyAgICB8LS5fICAgICAgICAgXy4tJwogICAgICAgICAgICAgICAgICAgICAgICAgICAgYC0uX3wtLl8gICAgIF8uLScgICAgICAgYF8uLSctLl9gLS5fIF8uLScKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYC0uX3wtLl8gICAgIF8uLScgICAgICAgYC0uX3wKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBgLS5ffC0uXyAgICAgICAgIF8uLScKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGAtLl8gXy4tJyAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIgo='

    print(base64.b64decode(something_cool).decode())

def main():
    print_something_cool()

if __name__ == "__main__":
    main()
