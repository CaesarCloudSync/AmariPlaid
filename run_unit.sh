if [[ $1 == "" ]]
then
  python -m unittest plaidunit.PlaidTestCase
else
  python -m unittest plaidunit.PlaidTestCase.$1
fi