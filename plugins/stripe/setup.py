from setuptools import setup, find_packages

setup(name='strokelitude_stripe',
      version='0.1',
      entry_points = {
    'strokelitude.plugins':[
    'StripeExperimentPluginInfo = stripe.experiment_runner:ExperimentRunnerPluginInfo',
    'StripePluginInfo = stripe.stripe:StripePluginInfo',
    ## 'SequencePluginInfo = stripe.sequence:SequencePluginInfo',
    ],
    },
      packages = find_packages(),
      author='Andrew Straw',
      author_email='strawman@astraw.com',
      )
