#include <iostream>
#include <vector>
#include <string>
#include <QtWidgets>

class BankAccount {
private:
    std::string accountNumber;
    std::string accountHolder;
    double balance;

public:
    BankAccount(const std::string& number, const std::string& holder, double initialBalance)
        : accountNumber(number), accountHolder(holder), balance(initialBalance) {}

    std::string getAccountNumber() const {
        return accountNumber;
    }

    std::string getAccountHolder() const {
        return accountHolder;
    }

    double getBalance() const {
        return balance;
    }

    void deposit(double amount) {
        balance += amount;
    }

    void withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
        }
    }
};

class MainWindow : public QMainWindow {
    Q_OBJECT

private:
    std::vector<BankAccount> accounts;
    QLabel* balanceLabel;

public:
    MainWindow(QWidget* parent = nullptr) : QMainWindow(parent) {
        // Create some bank accounts
        BankAccount account1("123456", "John Doe", 1000.0);
        BankAccount account2("789012", "Jane Smith", 5000.0);
        BankAccount account3("345678", "Bob Johnson", 200.0);

        // Add the accounts to the vector
        accounts.push_back(account1);
        accounts.push_back(account2);
        accounts.push_back(account3);

        // Create the main window
        QWidget* centralWidget = new QWidget(this);
        QVBoxLayout* layout = new QVBoxLayout(centralWidget);
        setCentralWidget(centralWidget);

        // Create the account selection combo box
        QComboBox* accountComboBox = new QComboBox(this);
        for (const auto& account : accounts) {
            accountComboBox->addItem(QString::fromStdString(account.getAccountNumber() + " - " + account.getAccountHolder()));
        }
        layout->addWidget(accountComboBox);

        // Create the balance label
        balanceLabel = new QLabel(this);
        layout->addWidget(balanceLabel);

        // Create the deposit and withdrawal buttons
        QPushButton* depositButton = new QPushButton("Deposit", this);
        QPushButton* withdrawButton = new QPushButton("Withdraw", this);
        layout->addWidget(depositButton);
        layout->addWidget(withdrawButton);

        // Connect the button signals to slots
        connect(depositButton, &QPushButton::clicked, this, &MainWindow::onDepositClicked);
        connect(withdrawButton, &QPushButton::clicked, this, &MainWindow::onWithdrawClicked);
        connect(accountComboBox, static_cast<void (QComboBox::*)(int)>(&QComboBox::currentIndexChanged),
                this, &MainWindow::onAccountChanged);

        // Initialize the balance label
        updateBalanceLabel(0);
        setWindowTitle("Banking Application");
    }

private slots:
    void onDepositClicked() {
        bool ok;
        double amount = QInputDialog::getDouble(this, "Deposit", "Amount:", 0.0, 0.0, 1000000.0, 2, &ok);
        if (ok) {
            int index = static_cast<QComboBox*>(centralWidget()->layout()->itemAt(0)->widget())->currentIndex();
            accounts[index].deposit(amount);
            updateBalanceLabel(index);
        }
    }

    void onWithdrawClicked() {
        bool ok;
        double amount = QInputDialog::getDouble(this, "Withdrawal", "Amount:", 0.0, 0.0, 1000000.0, 2, &ok);
        if (ok) {
            int index = static_cast<QComboBox*>(centralWidget()->layout()->itemAt(0)->widget())->currentIndex();
            accounts[index].withdraw(amount);
            updateBalanceLabel(index);
        }
    }

    void onAccountChanged(int index) {
        updateBalanceLabel(index);
    }

private:
    void updateBalanceLabel(int index) {
        const BankAccount& account = accounts[index];
        balanceLabel->setText("Account Holder: " + QString::fromStdString(account.getAccountHolder()) +
                              "\nCurrent Balance: $" + QString::number(account.getBalance(), 'f', 2));
    }
};

int main(int argc, char* argv[]) {
    QApplication app(argc, argv);

    MainWindow mainWindow;
    mainWindow.show();

    return app.exec();
}

#include "main.moc"
