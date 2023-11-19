import abc
import datetime


class Membership(abc.ABC):
    def __init__(self):
        self.fitness_cnt = 0
        self.massage_cnt = 0
        self.pool_cnt = 0


class Standard(Membership):
    def __init__(self):
        self.fitness_cnt = 12
        self.massage_cnt = 1
        self.pool_cnt = 6


class Premium(Membership):
    def __init__(self):
        self.fitness_cnt = 24
        self.massage_cnt = 2
        self.pool_cnt = 12


class AllIncluded(Membership):
    def __init__(self):
        self.fitness_cnt = None
        self.massage_cnt = None
        self.pool_cnt = None


class Member:
    def __init__(self, name: str, contact_info: str, membership_lvl: str, membership: Membership):
        self.name = name
        self.contact_info = contact_info
        self.membership_lvl = membership_lvl
        self.meme_duration = 30
        self.usage_log = dict(fitness=[0, None], pool=[0, None], massage=[0, None])
        self.statistics = ''


class System:
    def calculate_fee(self, member: Member):
        if member.membership_lvl == 'standard':
            rate = 0.2
        elif member.membership_lvl == 'premium':
            rate = 0.4
        elif member.membership_lvl == 'all included':
            rate = 0.6
        else:
            print('No such type of membership level')
        fee = 2400000 * 1 / 12 * rate
        print(f'Monthly fee of {member.membership_lvl}level membership is {fee} ')
        return fee

    def enter(self, member: Member, membership: Membership, area: str):
        if area == 'fitness':
            if member.usage_log['fitness'][0] < membership.fitness_cnt:
                member.usage_log['fitness'][0] += 1
                member.usage_log[area][1] = datetime.datetime.now()
            else:
                print('You have no access to fitness area')
        if area == 'pool':
            if member.usage_log['pool'][0] < membership.pool_cnt:
                member.usage_log['pool'][0] += 1
                member.usage_log[area][1] = datetime.datetime.now()
            else:
                print('You have no access to pool area')

        if area == 'massage':
            if member.usage_log['massage'][0] < membership.massage_cnt:
                member.usage_log['massage'][0] += 1
                member.usage_log[area][1] = datetime.datetime.now()
            else:
                print('You have no access to massage area')

        print(f'f{member.name} entered {area} area')

    def generate_statistics(self, member):
        member.statistics += f"{member.name}'s monthly statistics of areas and entries count\n"
        for i in member.usage_log.keys():
            print(f'Area:{i}, entry counts: {member.usage_log[i][0]}, entry time:{member.usage_log[i][1]}')

    def change_lvl(self, member, new_lvl):
        if new_lvl.lower() in ['standard', 'premium', 'all included']:
            member.membership_lvl = new_lvl
        else:
            print('No such level')

    def generate_bill(self, member):
        f = open(f"{member.name}'s bill.txt", 'a')
        f.write(member.statistics)
        f.write(f"Monthly fee of {member.name}")
        f.write(str(sys.calculate_fee(member)))


st = Standard()
member = Member('Anna', '+541651653', 'standard', st)
sys = System()
sys.calculate_fee(member)
sys.enter(member, st, 'pool')
sys.generate_statistics(member)
sys.generate_bill(member)
sys.change_lvl(member, 'all included')