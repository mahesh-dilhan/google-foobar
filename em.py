

def solution(l):
    elevators = []
    for elevator in l:
        elevators.append(Elevator(elevator))
    elevators.sort()
    return [el.str for el in elevators]

class Elevator:
    def __init__(self, elevator):
        divisor = list(map(int, elevator.strip().split('.')))
        self.str = elevator
        self.major = divisor[0]
        self.minor = divisor[1] if len(divisor) > 1 else -1
        self.revision = divisor[2] if len(divisor) > 2 else -1

    def __lt__(self, other):
        if self.major < other.major: return True
        if self.major > other.major: return False
        if self.minor < other.minor: return True
        if self.minor > other.minor: return False
        if self.revision < other.revision: return True
        if self.revision > other.revision: return False

if __name__ == "__main__":
    l1 = {"1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"}
    print(solution(l1))

    l2 = {"1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"}
    print(solution(l2))