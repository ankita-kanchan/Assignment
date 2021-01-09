#contants
APPROVED = "Approved"
APPLIED = "Applied"
VERIFIED = "Verified"
MAX = 10
MEMBER_REF = "memberRef"
UPDATE = "Update"
APP_STATUS = "appStatus"


class Hashtable:

    def __init__(self):
        self.table = [[] for _ in range(MAX)] #Hashtable initialization

    def hashId(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % MAX

    def insert(self, newItem):
        hash_key = self.hashId(newItem[0])
        self.table[hash_key].append(newItem)

    def update(self, key, updatedItem):
        hash_key = self.hashId(key)
        entry = self.table[hash_key]
        if len(entry) != 0:
            for i in range(len(entry)):
                if entry[i][0] == key:
                    result = list(set(updatedItem) - set(entry[i]))[0]
                    del entry[i]
                    entry.append(updatedItem)
                    break
            return result
        else:
            print('Item with given key is not present...')

    def delete(self, key):
        hash_key = self.hashId(key)
        entry = self.table[hash_key]
        updatedEntry = []
        if len(entry) != 0:
            for item in entry:
                if item[0] != key:
                    updatedEntry.append(item)
        else:
            print('Item with given key is not present...')

        self.table[hash_key] = updatedEntry

    def get(self, key):
        hash_key = self.hashId(key)
        entry = self.table[hash_key]
        if len(entry) != 0:
            for item in entry:
                if item[0] == key:
                    return item
            print("key is not present...")
        else:
            print('Item with given key is not present...')

    def destroy(self):
        self.table = [[] for _ in range(MAX)]

    def getAll(self):
        return self.table.copy()

    def size(self):
        totalSize = 0
        for entry in self.table:
            if len(entry) != 0:
                for item in entry:
                    totalSize += 1
        return totalSize


class ClubHouse:

    def __init__(self):
        self.initializeHash()

    def initializeHash(self):
        self.hash_table = Hashtable() #creates an empty hash table and points to null

    def insertAppDetails(self, name, phone, memRef, status):
        data =  [name, phone, memRef, status]
        self.hash_table.insert(data)

    def updateAppDetails(self, name, phone, memRef, status):
        data = [name,  phone,  memRef,  status]
        return self.hash_table.update(name, data)

    def memRef(self, memId):
        applicants = []
        for entry in self.hash_table.getAll():
            if len(entry) != 0:
                for item in entry:
                    if item[2].strip() == memId:
                        applicants.append(
                            "{name} / {phone} / {status}".format(name=item[0], phone=item[1],
                                                                 status=item[3]))
        return applicants

    def appStatus(self):
        Verified_count = 0
        Applied_count = 0
        Approved_count = 0
        for entry in self.hash_table.getAll():
            if len(entry) != 0:
                for item in entry:
                    Verified_count = Verified_count + sum(map((VERIFIED).__eq__, item))
                    Applied_count = Applied_count + sum(map((APPLIED).__eq__, item))
                    Approved_count = Approved_count + sum(map((APPROVED).__eq__, item))
        count =  [Approved_count, Applied_count, Verified_count]
        return count

    def destroyHash(self):
        self.hash_table.destroy()   #destroys all the entries inside hash table.

    def size(self):
        return self.hash_table.size()


def perform_update():
    try:
        data = i.replace("Update:", "").strip().split("/")
        output = clubHouse.updateAppDetails(data[0].strip(), data[1].strip(), data[2].strip(), data[3].strip())
        output_file.write("Updated details of {}. Application {} has been changed.\n".format(data[0].strip(), output))
    except Exception:
        output_file.write("Error Occured while performing update operation\n")


def perform_memberRef():
    try:
        memId = i.replace("memberRef:", "").strip()
        applicants = clubHouse.memRef(memId)
        output = "---------- Member reference by " + memId + " ----------\n"
        for applicant in applicants:
            output += applicant + "\n"
        output += "-------------------------------------\n"
        output_file.write(output)
    except Exception:
        output_file.write("Error Occured while performing memberRef operation\n")


def perform_appstatus():
    try:
        count = clubHouse.appStatus()
        output_file.write(
            "---------- Application Status ----------\nApplied:{0}\nVerified: {1}\nApproved: {2}\n-------------------------------------\n".format(
                count[1], count[2], count[0]))
    except Exception:
        output_file.write("Error Occured while performing appStatus operation\n")


try:
    #input File Open
    file = open("inputPS26.txt", "r")
    applicant_data = file.readlines()

    clubHouse = ClubHouse() #created object of Clubhouse class
    output_file = open("outputPS26.txt", "w")

    for i in applicant_data:
        line = i.strip("\n").strip().split("/")
        clubHouse.insertAppDetails(line[0].strip(), line[1].strip(), line[2].strip(), line[3].strip())

    output_file.write("Successfully inserted {} applications into the system.\n".format(clubHouse.size()))

    p_file = open("promptsPS26.txt", "r")
    prompt_data = p_file.readlines()

    for i in prompt_data:
        promptLine = i.split(":")
        command = promptLine[0].strip()

        if command == UPDATE:
            perform_update()

        elif command == MEMBER_REF:
            perform_memberRef()

        elif command == APP_STATUS:
            perform_appstatus()

        else:
            output_file.write("Operation not supported - {}\n".format(command))

    #closing text files
    file.close()
    output_file.close()

except Exception as e:
    print("Error occured")
