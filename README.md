### **Simple Password Checker (Loop Example)** <br>

This Python script demonstrates a simple password authentication mechanism using a **`while` loop** and a **`break` statement**. It also includes a **limit on the number of attempts** (3 attempts) to make it more robust.<br>

---<br>

### ** Updated Code Implementation**<br>

Here is how you would update your `2.py` file to include the attempt limit:<br>

```python
current_password = "Pratham"<br>
max_attempts = 3<br>
attempt_count = 0<br>

while attempt_count < max_attempts:<br>
    user_password = input("Enter Your Password : ")<br>
    attempt_count = attempt_count + 1<br>

    if current_password == user_password.strip():<br>
        print("Correct Password, Congrats!")<br>
        break<br>
    elif attempt_count < max_attempts:<br>
        print(f"Invalid password. You have {max_attempts - attempt_count} attempts left.")<br>
    else:<br>
        print("Invalid password. All attempts used.")<br>

if current_password == user_password.strip():<br>
    print("logged in")<br>
else:<br>
    print("Access Denied!")<br>
```<br>

---<br>

### ** Changes & Concepts**<br>

1.  **`max_attempts`**: Defines the total number of tries (set to 3).<br>
2.  **`attempt_count`**: A variable initialized to 0 that **increments** with every wrong attempt.<br>
3.  **`while attempt_count < max_attempts`**: The loop now continues only as long as the counter is less than the limit, providing the boundary.<br>
4.  **`elif` Condition**: Checks if the user is out of attempts *before* printing the remaining attempts.<br>
5.  **Final Check**: The `if/else` block outside the loop determines the final status ("logged in" or "Access Denied!") after the loop finishes.<br>

---<br>

### ** How to Run the Script**<br>

#### **Prerequisites**<br>

You need **Python 3** installed on your system.<br>

#### **Running the Script**<br>

1.  **Save the file:** Save the code as `password_check.py`.<br>
2.  **Open Terminal:** Navigate to the script's directory.<br>
3.  **Execute:** Run the script:<br>
    ```bash
    python password_check.py
    ```<br>

#### **How to Use**<br>

* The script will prompt you for the password.<br>
* If you fail to enter **"Pratham"** within **3 tries**, the script will exit and display **"Access Denied!"**.<br>
