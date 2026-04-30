import csv


# Load the CSV file
# Load the CSV file and store the file name in a variable for easy modification later/加载CSV文件，把文件名存在一个变量里，方便以后修改
filename = "demo_responses.csv"
responses = []


# 打开CSV文件并逐行读取，每一行会自动变成一个字典（列名对应值）/Open the CSV file and read it line by line. Each line will automatically be converted into a dictionary (with column names corresponding to values).
with open(filename, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        responses.append(row)

# any inline comments yep let me try chinese now 中文也可以呢
# Yeah I can see that inline comments above!



# 定义一个函数：计算一段文字里有多少个单词/Define a function: count the number of words in a response string
def count_words(response):
    """Count the number of words in a response string.

    Takes a string, splits it on whitespace, and returns the word count.
    Used to measure response length across all participants.
    """
    return len(response.split())


# Count words in each response and print a row-by-row summary
print(f"{'ID':<6} {'Role':<22} {'Words':<6} {'Response (first 60 chars)'}")
print("-" * 75)

word_counts = []

for row in responses:
    participant = row["participant_id"]
    role = row["role"]
    response = row["response"]

    # Call our function to count words in this response
    count = count_words(response)
    word_counts.append(count)

    # Truncate the response preview for display
    if len(response) > 60:
        preview = response[:60] + "..."
    else:
        preview = response

    print(f"{participant:<6} {role:<22} {count:<6} {preview}")

# Print summary statistics
print()
print("── Summary ─────────────────────────────────")
print(f"  Total responses : {len(word_counts)}")
print(f"  Shortest        : {min(word_counts)} words")
print(f"  Longest         : {max(word_counts)} words")
print(f"  Average         : {sum(word_counts) / len(word_counts):.1f} words")
