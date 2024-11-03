import pyodbc

# Database connection details
server = '172.16.64.245'
database = 'sybase'
username = 'BASIS'
password = 'Kamran@200786'

connection = pyodbc.connect(
    "DRIVER={Sybase ASE ODBC Driver};SERVER=your_server_name;PORT=your_port;UID=your_username;PWD=your_password;DATABASE=your_database;PacketSize=8192"
)


# Connection establish karna
try:
    conn = pyodbc.connect(f'DRIVER={{Adaptive Server Enterprise}};SERVER={server};DATABASE={database};UID={username};PWD={password};')
    cursor = conn.cursor()
    print("Connection established successfully.")
except Exception as e:
    print("An error occurred while connecting to the database:", e)
    exit()  # Agar connection nahi hota, to exit kar dena

# Max packet size set karne ka SQL command
try:
    # Max packet size update karne ka command
    cursor.execute("sp_configure 'max packet size', 16384;")  # 16384 bytes ka example
    cursor.execute("RECONFIGURE;")  # Configuration apply karna
    print("Max packet size updated to 16384 bytes.")
except Exception as e:
    print("An error occurred while updating max packet size:", e)

# Ab data retrieve karne ka command
try:
    cursor.execute("SELECT * FROM ekko where aedate = 20102024;")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
except Exception as e:
    print("An error occurred while fetching data:", e)

# Connection band karna
finally:
    cursor.close()
    conn.close()
