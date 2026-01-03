age=int(input("Enter the age="))
citizen=input("Are you citizen(Yes/No)=").strip().lower()
is_citizen=citizen=="yes"
if age>=18 and is_citizen:
    print("\nYou are Eligible for vote.")
else:
    print("\nYou are not Eligible for vote")
