{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a2c175e5-877b-43a7-9798-f7a86bb0308e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "===== STUDENT MANAGEMENT SYSTEM =====\n",
      "1. Add Student\n",
      "2. View Students\n",
      "3. Search Student\n",
      "4. Delete Student\n",
      "5. Save to File\n",
      "6. Load from File\n",
      "7. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Students saved successfully!\n",
      "\n",
      "===== STUDENT MANAGEMENT SYSTEM =====\n",
      "1. Add Student\n",
      "2. View Students\n",
      "3. Search Student\n",
      "4. Delete Student\n",
      "5. Save to File\n",
      "6. Load from File\n",
      "7. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Students loaded successfully!\n",
      "\n",
      "===== STUDENT MANAGEMENT SYSTEM =====\n",
      "1. Add Student\n",
      "2. View Students\n",
      "3. Search Student\n",
      "4. Delete Student\n",
      "5. Save to File\n",
      "6. Load from File\n",
      "7. Exit\n"
     ]
    }
   ],
   "source": [
    "students=[]\n",
    "def add_student():\n",
    "    name=input(\"Enter student name:\")\n",
    "    age=int(input(\"Enter student age:\"))\n",
    "    course=input(\"Enter student course:\")\n",
    "    student={\n",
    "    \"name\": name,\n",
    "    \"age\": age,\n",
    "    \"course\":course\n",
    "    }   \n",
    "    students.append(student)\n",
    "    print(\"Student added Successfully!\")\n",
    "def view_students():\n",
    "    print(\"\\n===== Students =====\")\n",
    "    for student in students:\n",
    "        print(\"Name:\",student[\"name\"])\n",
    "        print(\"Age:\",student[\"age\"])\n",
    "        print(\"Course:\",student[\"course\"])\n",
    "        print()\n",
    "def search_students():\n",
    "    search_name=input(\"Enter student name:\").lower()\n",
    "    found = False\n",
    "    for student in students:\n",
    "        if student[\"name\"].lower()==search_name:\n",
    "            print(\"Student Found.\")\n",
    "            print(\"Name:\",student[\"name\"])\n",
    "            print(\"Age:\",student[\"age\"])\n",
    "            print(\"Course:\",student[\"course\"])\n",
    "            found=True\n",
    "    if found == False:\n",
    "            print(\"Student not found.\")\n",
    "def delete_student():\n",
    "    delete_name=input(\"Enter student name to delete:\").lower()\n",
    "    found=False\n",
    "    for student in students:\n",
    "        if student[\"name\"].lower()==delete_name:  \n",
    "            students.remove(student) \n",
    "            found=True\n",
    "            print(\"Student record deleted.\")\n",
    "            break   \n",
    "    if found== False:\n",
    "            print(\"Student not found.\")\n",
    "        \n",
    "def save_students(students):\n",
    "    with open(\"students.txt\", \"w\") as file:\n",
    "            for student in students:\n",
    "                file.write(student[\"name\"] + \" | \" + str(student[\"age\"]) + \" | \" + student[\"course\"] + \"\\n\")\n",
    "    print(\"Students saved successfully!\")            \n",
    "def load_students():\n",
    "    students = []\n",
    "    with open(\"students.txt\", \"r\") as file:\n",
    "        for line in file:\n",
    "            parts = line.split(\"|\")\n",
    "            student = {\n",
    "                \"name\": parts[0].strip(),\n",
    "                \"age\": int(parts[1].strip()),\n",
    "                \"course\": parts[2].strip()\n",
    "            }\n",
    "\n",
    "            students.append(student)\n",
    "\n",
    "    return students\n",
    "def menu():\n",
    "    print(\"\\n===== STUDENT MANAGEMENT SYSTEM =====\")\n",
    "    print(\"1. Add Student\")\n",
    "    print(\"2. View Students\")\n",
    "    print(\"3. Search Student\")\n",
    "    print(\"4. Delete Student\")\n",
    "    print(\"5. Save to File\")\n",
    "    print(\"6. Load from File\")\n",
    "    print(\"7. Exit\")\n",
    "while True:\n",
    "    menu()\n",
    "\n",
    "    choice = input(\"Enter your choice: \")\n",
    "    \n",
    "    if choice == \"1\":\n",
    "        add_student()\n",
    "    elif choice == \"2\":\n",
    "        view_students()\n",
    "    elif choice ==\"3\":\n",
    "        search_students()\n",
    "    elif choice == \"4\":\n",
    "        delete_student()\n",
    "    elif choice ==\"5\":\n",
    "        save_students(students)\n",
    "    elif choice ==\"6\":\n",
    "        students = load_students()\n",
    "        print(\"Students loaded successfully!\")\n",
    "    elif choice ==\"7\":\n",
    "        print(\"Thank you for using Student Management System!\")\n",
    "        break\n",
    "    else:\n",
    "        print(\"Invalid choice. Please enter a number from 1 to 7.\")\n",
    "    \n",
    "\n",
    "\n",
    "   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e23d5edc-6789-4d06-91b4-f8a47eba2d23",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01afd2b3-55eb-443d-85ec-638abc3bcfe8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
