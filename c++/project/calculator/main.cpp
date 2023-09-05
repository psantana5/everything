#include <QApplication>
#include <QWidget>
#include <QGridLayout>
#include <QPushButton>
#include <QLineEdit>
#include <QWebEngineView>
#include <QWebChannel>

#include <QString>
#include <QScriptEngine>

#include <QDebug>

class CalculatorInterface : public QObject
{
    Q_OBJECT

public:
    CalculatorInterface(QObject *parent = nullptr) : QObject(parent) {}

public slots:
    void evaluateExpression(const QString &expression)
    {
        // Evaluate the expression and display the result in C++
        qDebug() << "Received expression from JavaScript:" << expression;

        // Use QScriptEngine to evaluate the expression
        QScriptEngine engine;
        QScriptValue result = engine.evaluate(expression);

        if (result.isValid() && result.isNumber()) {
            // Convert the result to a string and emit the signal
            QString resultString = result.toString();
            qDebug() << "Result:" << resultString;

            emit resultCalculated(resultString);
        } else {
            emit resultCalculated("Error");
        }
    }

signals:
    void resultCalculated(const QString &result);
};

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    // Create the main window
    QWidget window;
    window.setWindowTitle("Calculator");
    window.setMinimumSize(400, 500);

    // Create the grid layout
    QGridLayout *layout = new QGridLayout(&window);

    // Create the web view for displaying the HTML file
    QWebEngineView *webView = new QWebEngineView(&window);
    layout->addWidget(webView, 0, 0, 1, 4);

    // Create a web channel to enable communication between C++ and JavaScript
    QWebChannel *webChannel = new QWebChannel(&window);
    webView->page()->setWebChannel(webChannel);

    // Create an instance of CalculatorInterface
    CalculatorInterface calculatorInterface;
    webChannel->registerObject("Qt", &calculatorInterface);

    // Connect the resultCalculated signal to a lambda function
    QObject::connect(&calculatorInterface, &CalculatorInterface::resultCalculated, [&calculatorInterface](const QString &result) {
        // Display the result in C++
        qDebug() << "Result:" << result;
    });

    // Load the HTML file
    webView->setUrl(QUrl::fromLocalFile("calculator.html"));

    window.setLayout(layout);
    window.show();

    return app.exec();
}

#include "main.moc"
