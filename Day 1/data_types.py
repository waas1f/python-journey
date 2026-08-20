{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c0d714b8-929d-4067-b2be-5774ef2d47f7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n",
      "<class 'int'>\n",
      "<class 'float'>\n",
      "<class 'bool'>\n"
     ]
    }
   ],
   "source": [
    "name = \"Muhammad Wasif\"\n",
    "age = 20\n",
    "income = 500.50\n",
    "student = True\n",
    "print(type(name))\n",
    "print(type(age))\n",
    "print(type(income))\n",
    "print(type(student))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9c855460-5908-4141-a29e-2e990f23f440",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Whats your age? 20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n"
     ]
    }
   ],
   "source": [
    "age = int(input(\"Whats your age?\"))\n",
    "print(type(age))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ba241f50-e5e8-47a2-9ded-0f3406b4703b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Whats your age? 20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Next year you will be 21\n"
     ]
    }
   ],
   "source": [
    "age = int(input(\"Whats your age?\"))\n",
    "next_year = age + 1\n",
    "print(\"Next year you will be\", next_year)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "11123afa-be3a-4a46-9a47-a2904461defa",
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
