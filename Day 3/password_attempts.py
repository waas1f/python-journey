{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "e1ed3bdd-7832-434a-950e-7d4086809370",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Password: wasif\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wrong Password\n",
      "Attempts Remining: 2\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Password python123\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome!\n"
     ]
    }
   ],
   "source": [
    "password = \"python123\"\n",
    "attempts = 3\n",
    "key = input(\"Enter Password:\")\n",
    "while key != password and attempts > 0:\n",
    "    print(\"Wrong Password\")\n",
    "    attempts -= 1\n",
    "    print(\"Attempts Remining:\",attempts)\n",
    "    key = input(\"Enter Password\")\n",
    "if key==password:\n",
    "    print(\"Welcome!\")\n",
    "else:\n",
    "    print(\"Access Denied\")\n",
    "\n",
    "    \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f6e047ae-96bd-4891-9844-e32de63bbd26",
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
