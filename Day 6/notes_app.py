{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fce3b42c-d357-4580-92d4-f793f75c9d50",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Write your note: Pythongo\n",
      "Do you want to add another note? (yes/no) yes\n",
      "Write your note: Gym\n",
      "Do you want to add another note? (yes/no) yes\n",
      "Write your note: Trading\n",
      "Do you want to add another note? (yes/no) Yes\n",
      "Write your note: Turkish\n",
      "Do you want to add another note? (yes/no) no\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "===== Your Notes =====\n",
      "Pythongo\n",
      "Gym\n",
      "Trading\n",
      "Turkish\n",
      "\n"
     ]
    }
   ],
   "source": [
    "note=input(\"Write your note:\")\n",
    "with open(\"notes.txt\",\"w\") as file:\n",
    "    file.write(note + \"\\n\")\n",
    "ask=input(\"Do you want to add another note? (yes/no)\").lower()\n",
    "while ask== \"yes\":\n",
    "    note=input(\"Write your note:\")\n",
    "    with open(\"notes.txt\",\"a\") as file:\n",
    "        file.write(note + \"\\n\")\n",
    "    ask=input(\"Do you want to add another note? (yes/no)\").lower()\n",
    "print(\"\\n===== Your Notes =====\")\n",
    "with open(\"notes.txt\",\"r\") as file:\n",
    "    content=file.read()\n",
    "print(content)    \n",
    "    \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef4cdea5-0b54-495c-bd68-5526471bdda1",
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
