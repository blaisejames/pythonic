import uuid, datetime

class Call(object):
    def __init__(self, caller, phone_num, reason):
        self.caller = caller
        self.phone_num = phone_num
        self.reason = reason
        self.id = uuid.uuid4()
        self.time = datetime.datetime.now()
        
    def display_info(self):
        print "\n"
        for attr, val in self.__dict__.iteritems():
            if attr == "time":
                print "{}: {}".format(attr, val.strftime("%I:%M:%S"))
            else:
                print "{}: {}".format(attr, val)

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = self.get_queue_size()

    def get_queue_size(self):
        return len(self.calls)

    def add(self, add_call):
        self.calls.append(add_call)
        return self

    def remove(self, rem_call):
        self.calls.remove(rem_call)

    def info(self):
        for call in self.calls:
            call.display_info()

call1 = Call("Mary Stout", "800-234-5687", "Needs a replacement part")
call2 = Call("Bilbo Baggins", "866-788-5667", "Can't find the ring")
call3 = Call("Janis Joplin", "567-888-7890", "Wants a Mercedes-Benz")
call4 = Call("Usher", "456-777-2222", "Wonders why they left the P off his first name")
center = CallCenter()
center.add(call1).add(call2).add(call3).add(call4).remove(call4)
center.info()
    