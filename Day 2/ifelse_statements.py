{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d87bd410-3304-4d62-a2de-c9d2b60357ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your age:  20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You can vote.\n"
     ]
    }
   ],
   "source": [
    "age=int(input(\"Enter your age: \"))\n",
    "if age >= 18:\n",
    "    print(\"You can vote.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7889e70c-35d0-4730-b544-ff58092562fd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your age:  19\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You are a teenager.\n"
     ]
    }
   ],
   "source": [
    "age=int(input(\"Enter your age: \"))\n",
    "if age <=19:\n",
    "    print(\"You are a teenager.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "56aa464b-9a6e-405c-b2e7-6c4e96e9a0a7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your age:  17\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Minor\n"
     ]
    }
   ],
   "source": [
    "age=int(input(\"Enter your age: \"))\n",
    "if age >=18:\n",
    "          print(\"Adult\")\n",
    "else:\n",
    "      print(\"Minor\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "7cb5b820-9b72-4472-977d-ab30ff8b8ac9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your marks:  55\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Need Improvement\n"
     ]
    }
   ],
   "source": [
    "marks=int(input(\"Enter your marks: \"))\n",
    "if marks >= 90:\n",
    "    print(\"Grade A\")\n",
    "elif marks >= 80:\n",
    "    print(\"Grade B\")\n",
    "elif marks >= 70:\n",
    "    print(\"Grade C\")\n",
    "elif marks >= 60:\n",
    "    print(\"Grade D\")\n",
    "else:\n",
    "    print(\"Need Improvement\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3625d375-2b9d-4610-96f0-d33b3250c51d",
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
