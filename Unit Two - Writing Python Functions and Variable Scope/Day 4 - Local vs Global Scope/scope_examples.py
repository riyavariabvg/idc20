global_book = "Encyclopedia of Science"

def section_book():
    global local_book
    local_book = "Chemistry Handbook"
    print(f"In the section: We have the {global_book} and the {local_book}")

section_book()

print(f"In the library: but not the {local_book}")
