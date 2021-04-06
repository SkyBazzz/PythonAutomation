from abc import ABCMeta
import logging

logger = logging.getLogger("Firm")

class Company:

    def __init__(self, name=None, address=None):
        self.name = name
        self.address = address
        self.employees = list()
        self.__money = 1000

    def add_employee(self, employee):
        if isinstance(employee, (Engineer, Manager)) and employee.company is None:
            self.employees.append(employee)

    def dismiss_employee(self, employee):
        if employee.company.name == self.name:
            self.employees.remove(employee)
            employee.company = None
            employee.notify_dismissed()

    def notify_im_leaving(self, employee):
        logger.debug(f"{employee.name} is leaving {self.name}")

    def do_tasks(self, employee):
        if employee.company.name == self.name and isinstance(employee, Engineer):
            employee.put_money_into_my_wallet(employee.SALARY)
            self.__money -= employee.SALARY

    def write_reports(self, employee):
        if employee.company.name == self.name and isinstance(employee, Manager):
            employee.put_money_into_my_wallet(employee.SALARY)
            self.__money -= employee.SALARY

    def make_a_party(self, bonus=5):
        if self.__money > 0:
            logger.debug(f"{self.name}. Party time! All employees get 5 money ")
            for employee in self.employees:
                employee.bonus_to_salary(self, bonus)
        if self.__money < 0:
            self.go_bankrupt()

    def show_money(self):
        logger.info(f"{self.name} has {self.__money}")

    @property
    def balance(self):
        return self.__money

    @balance.setter
    def balance(self, money):
        self.__money -= money

    def go_bankrupt(self):
        logger.debug(f"{self.name} went bankrupt")
        logger.debug(self.employees)
        self.__money = 0
        for employee in self.employees:
            employee.notify_dismissed()
            employee.become_unemployed()
        self.employees.clear()

    def is_bankrupt(self):
        return self.__money <= 0

    def __repr__(self):
        return 'Company (%s)' % self.name


class Person:

    def __init__(self, name, age, sex=None, address=None):
        self.name = name
        self.age = age
        self.address = sex if sex is not None else '<not specified>'
        self.sex = address

    def __repr__(self):
        return '%s, %s years old' % (self.name, self.age)


class Employee(Person):
    __metaclass__ = ABCMeta
    SALARY = 3

    def __init__(self, name, age, sex=None, address=None):
        super().__init__(name, age, sex, address)
        self.company = None
        self.__money = 0

    def join_company(self, company):
        if self.is_employed:
            logger.debug(f'Ups, {self.name} is already haired')
        else:
            company.add_employee(self)
            self.company = company
            logger.debug(f"{self.name} joined company {company.name}")

    def become_unemployed(self):
        logger.debug(f"{self.name} became unemployed")
        self.company.notify_im_leaving(self)
        self.company.employees.remove(self)
        logger.debug(f"Leaving company {self.company.name}")
        self.company = None

    def notify_dismissed(self):
        logger.debug(f"{self.name} is dismissed ")

    def bonus_to_salary(self, company, reward=5):
        if self.company.name == company.name:
            self.__money += reward
            company.balance = reward
            logger.debug(f"{self.name} got bonus({reward}) to salary")

    @property
    def is_employed(self):
        return self.company is not None

    def show_money(self):
        logger.info(f"{self.name} has {self.__money}")

    def put_money_into_my_wallet(self, amount):
        self.__money += amount

    def do_work(self):
        self.put_money_into_my_wallet(self.SALARY)
        self.company.balance = self.SALARY
        logger.debug(f"{self.name} did some work + {self.SALARY}")

    def __repr__(self):
        if self.is_employed:
            return f"{self.name} works at {self.company}"
        return f'{self.name}, unemployed'


class Engineer(Employee):
    SALARY = 10

    def do_work(self):
        super().do_work()


class Manager(Employee):
    SALARY = 12

    def do_work(self):
        super().do_work()
