from abc import ABC, abstractmethod


class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, data: dict) -> bool:
        pass


class PayPallPaymentStrategy(PaymentStrategy):

    def pay(self, data: dict) -> bool:
        # work with data
        print('working with PayPall payment api')
        print(data)
        return True


class CreditCardPaymentStrategy(PaymentStrategy):

    def pay(self, data: dict) -> bool:
        # work with data
        print('working with Credit Card payment api')
        print(data)
        return True


class WebMoneyPaymentStrategy(PaymentStrategy):

    def pay(self, data: dict) -> bool:
        # work with data
        print('working with  WebMoney payment api')
        print(data)
        return True


class Order:

    def pay(self, data: dict, payment_strategy: PaymentStrategy):
        payment_strategy.pay(data=data)


if __name__ == '__main__':
    o = Order()
    payment_method = input("How do you want to pay, with PayPall, WebMoney or CreditCard")
    payment_strategy: PaymentStrategy = None
    data = None
    if payment_method == "pp":
        pay_pall_email = input("enter pay pall email")
        data = dict(pp_email=pay_pall_email)
        payment_strategy = PayPallPaymentStrategy()
    elif payment_method == 'wm':
        vm_number = input("enter your web money account")
        data = dict(wm_number=vm_number)
        payment_strategy = WebMoneyPaymentStrategy()
    elif payment_method == "cc":
        cc_number = input("enter your credit card number")
        cc_date = input("enter your credit card date")
        data = dict(cc_number=cc_number, cc_date=cc_date)
        payment_strategy = CreditCardPaymentStrategy()
    else:
        print("Wrong payment method. Please try again")

    o.pay(data=data, payment_strategy=payment_strategy)
