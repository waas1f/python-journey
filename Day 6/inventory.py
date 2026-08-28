{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "fb9bcf4c-fb98-41c0-be2e-0822509ece7e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Laptop Stock: 5\n",
      "Mouse Stock: 25\n",
      "Keyboard Stock: 20\n"
     ]
    }
   ],
   "source": [
    "inventory={\n",
    "    \"laptop\":\"5\",\n",
    "    \"mouse\":\"15\",\n",
    "    \"keyboard\":\"20\"\n",
    "}\n",
    "inventory.update({\n",
    "    \"mouse\":\"25\"\n",
    "})    \n",
    "print(\"Laptop Stock:\",inventory[\"laptop\"])\n",
    "print(\"Mouse Stock:\",inventory[\"mouse\"])\n",
    "print(\"Keyboard Stock:\",inventory[\"keyboard\"])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a3d9fcff-da0b-4065-9219-89f2dc8eabaf",
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
