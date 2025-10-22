def chai_flavor(flavor="masala"):
    """Return the flavour of chai"""
    return flavor


print(chai_flavor.__doc__)
print(chai_flavor.__name__)


def gnerate_bill(chai=0 , samosa=0):
    """
    calculate the total bill for chai ans samosa
    
    :param chai:Number of chai cups(10 rupess each)
    :param samosa: Number of samosa (15 rupees each)
    :return (total amount , thankyou message)
    
    """
    total = chai*10+samosa*15
    return total, "Thank you visting chaicode.com"


