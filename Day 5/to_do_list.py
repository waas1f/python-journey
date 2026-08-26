{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "99d77987-e448-4a07-a5d5-25b230b26e1c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Task 1: Gym\n",
      "Enter Task 2: turkish\n",
      "Enter Task 3: sleeping\n",
      "Enter Task 4: Party\n",
      "Enter Task 5: Github\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Your To-Do List\n",
      "1 . Gym\n",
      "2 . turkish\n",
      "3 . sleeping\n",
      "4 . Party\n",
      "5 . Github\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Do you want add another task? (yes/no) yes\n",
      "Enter Task: Python\n",
      "Do you want add another task? (yes/no) no\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Your Updated To-Do List\n",
      "1 . Gym\n",
      "2 . turkish\n",
      "3 . sleeping\n",
      "4 . Party\n",
      "5 . Github\n",
      "6 . Python\n",
      "Thank You!\n"
     ]
    }
   ],
   "source": [
    "to_do_list=[]\n",
    "for i in range(5):\n",
    "    task=input (f\"Enter Task {i+1}:\")\n",
    "    to_do_list.append(task)\n",
    "print(\"\\nYour To-Do List\")\n",
    "for i in range(len(to_do_list)):\n",
    "    print(i+1,\".\",to_do_list[i])\n",
    "add_task=input(\"Do you want add another task? (yes/no)\").lower()\n",
    "while add_task==\"yes\":\n",
    "    task=input(\"Enter Task:\")\n",
    "    to_do_list.append(task)\n",
    "    add_task=input(\"Do you want add another task? (yes/no)\").lower()    \n",
    "print(\"\\nYour Updated To-Do List\")  \n",
    "for i in range(len(to_do_list)):\n",
    "    print(i+1,\".\",to_do_list[i])\n",
    "print(\"Thank You!\")\n",
    "    \n",
    "    \n",
    "    \n",
    "          \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "80547c27-d74e-4dbb-9ed3-c561cf44d6e1",
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
