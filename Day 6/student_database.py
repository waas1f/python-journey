{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "28aa0e90-5d3f-4d5d-8863-8292c6515f82",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Whats your name? Wasif\n",
      "Whats your age? 20\n",
      "In which university are you in? Beykoz\n",
      "In which country do you live? Turkey\n",
      "In which program are you enrolled? Computer Engineering\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "===== Student Profile ====\n",
      "Name: Wasif\n",
      "Age: 20\n",
      "University: Beykoz\n",
      "Country: Turkey\n",
      "Program: Computer Engineering\n",
      "\n"
     ]
    }
   ],
   "source": [
    "def save_student(bio):\n",
    "    with open(\"student.txt\",\"w\") as file:\n",
    "        file.write(\"Name: \" + bio[\"name\"] + \"\\n\")\n",
    "        file.write(\"Age: \" + str(bio[\"age\"]) + \"\\n\")\n",
    "        file.write(\"University: \" + bio[\"university\"] + \"\\n\")\n",
    "        file.write(\"Country: \" + bio[\"country\"] + \"\\n\")\n",
    "        file.write(\"Program: \" + bio[\"program\"] + \"\\n\")\n",
    "bio = {\n",
    "    \"name\":input(\"Whats your name?\"),\n",
    "    \"age\":int(input(\"Whats your age?\")),\n",
    "    \"university\":input(\"In which university are you in?\"),\n",
    "    \"country\":input(\"In which country do you live?\"),\n",
    "    \"program\":input(\"In which program are you enrolled?\")\n",
    "}    \n",
    "print(\"\\n===== Student Profile ====\")\n",
    "with open(\"student.txt\",\"r\") as file:\n",
    "    content=file.read()\n",
    "print(content)    \n",
    "save_student(bio)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "97a13b45-b0c3-4654-bce2-d865f9c79da6",
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
