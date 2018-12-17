from seneca.libs.datatypes import hmap

balances = hmap('balances', str, int)
allowed = hmap('allowed', str, hmap(value_type=int))
market = hmap('market', str, int)

@seed
def deposit_to_all_wallets():
    market['stamps_to_tau'] = 1
    assert market['stamps_to_tau'] == 1, 'whaaaaaathjgklg'
    balances['black_hole'] = 0

    STU = ('db929395f15937f023b4682995634b9dc19b1a2b32799f1f67d6f080b742cdb1',
           '324ee2e3544a8853a3c5a0ef0946b929aa488cbe7e7ee31a0fef9585ce398502')
    DAVIS = ('21fee38471799f8c2989dd81c6d46f6c2e2db6caf63efa98a093fcba064a4b62',
             'a103715914a7aae8dd8fddba945ab63a169dfe6e37f79b4a58bcf85bfd681694')
    DENTON = ('9decc7f7f0b5a4fc87ab5ce700e2d6c5d51b7565923d50ea13cbf78031bb3acf',
              '20da05fdba92449732b3871cc542a058075446fedb41430ee882e99f9091cc4d')
    FALCON = ('bac886e7c6e4a9fae572e170adb333b27b590157409e62d88cc0c7bc9a7b3631',
              'ed19061921c593a9d16875ca660b57aa5e45c811c8cf7af0cfcbd23faa52cbcd')
    CARL = ('cf67a180f9578afa5fd704cea39b450c1542755d73614f6a4f41b627190b83bb',
            'cb9bfd4b57b243248796e9eb90bc4f0053d78f06ce68573e0fdca422f54bb0d2')
    RAGHU = ('b44a8cc3dcadbdb3352ea046ec85cd0f6e8e3f584e3d6eb3bd10e142d84a9668',
             'c1f845ad8967b93092d59e4ef56aef3eba49c33079119b9c856a5354e9ccdf84')

    SEED_AMOUNT = 2 ** 63
    ALL_WALLETS = [STU, DAVIS, DENTON, FALCON, CARL, RAGHU]

    # this is hella silly lmao look what i have to do to just to seed a list of wallets. we should really just allow
    # for loops, i see little point in disallowing them
    def seed_wallet(wallet):
        print('seeding wallet {}'.format(wallet[1]))
        balances[wallet[1]] = SEED_AMOUNT
    list(map(seed_wallet, ALL_WALLETS))

    balances[STU[1]] = SEED_AMOUNT
    assert balances.get(STU[1]) == SEED_AMOUNT, "Seeding did not work!"
    assert balances.get(DAVIS[1]) == SEED_AMOUNT, "Seeding did not work!"

@export
def submit_stamps(stamps):
    amount = stamps / market['stamps_to_tau']
    transfer('black_hole', int(amount))

@export
def balance_of(wallet_id):
    return balances[wallet_id]

@export
def transfer(to, amount):
    # print("transfering from {} to {} with amount {}".format(rt['sender'], to, amount))
    balances[rt['sender']] -= amount
    balances[to] += amount
    sender_balance = balances[rt['sender']]

    assert sender_balance >= 0, "Sender balance must be non-negative!!!"

@export
def approve(spender, amount):
    allowed[rt['sender']][spender] = amount


@export
def transfer_from(_from, to, amount):
    assert allowed[_from][rt['sender']] >= amount
    assert balances[_from] >= amount

    allowed[_from][rt['sender']] -= amount
    balances[_from] -= amount
    balances[to] += amount


@export
def allowance(approver, spender):
    return allowed[approver][spender]


@export
def mint(to, amount):
    # print("minting {} to wallet {}".format(amount, to))
    assert rt['sender'] == rt['author'], 'Only the original contract author can mint!'

    balances[to] += amount

