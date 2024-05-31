import sys
import requests
import json
url = "http://localhost:11434/api/chat"

def llama3(prompt):
    data = {
        "model": "llama3",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=data)
    return (response.json()['message']['content'])

# code= """
# import java.util.Scanner;
# public class PrimeChecker {
#     public static void main(String[] args) {
#         Scanner scanner = new Scanner(System.in);
#         System.out.println("Enter a number: ");
#         int num = scanner.nextInt();
#         if (isPrime(num)) {
#             System.out.println(num + " is a prime number.");
#         } else {
#             System.out.println(num + " is not a prime number.");
#         }
#     }
#     public static boolean isPrime(int n) {
#         if (n <= 1) {
#             return false;
#         }
#         for (int i = 2; i * i <= n; i++) {
#             if (n % i == 0) {
#                 return false;
#             }
#         }
#         return true;
#     }
# }
# """

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py <file_name>")
        sys.exit(1)
    code_file = sys.argv[1]
    language = sys.argv[2]
    user_prompt = sys.argv[3]
    with open(code_file,'r') as file:
        file_contents = file.read()
    prompt = f"{user_prompt} {language} : {file_contents}"
    response = llama3(prompt)
    print(response)