from cloudify import ctx
from cloudify.state import ctx_parameters as inputs
from datetime import datetime, timedelta
from time import sleep
from cloudify.decorators import operation


@operation
def write_to_file(*args, **kwargs):
    with open('/tmp/cloudify-plugin', 'w') as f:
        f.write('This simple example gives you the power to do amazing things.\n')

@operation(resumable=True)
def tick(ctx, **kwargs):
    test_time = int(inputs.get('test_time', 30))
    end_time = datetime.now() + timedelta(0,test_time)
    while True:
        current_data = str(datetime.now())
        ctx.logger.info("test_func: {}".format(current_data))
        if ctx.instance.runtime_properties.get('data'):
            ctx.logger.info("runtime test_func: {}".format(ctx.instance.runtime_properties.get('data')))
        else:
            ctx.logger.info("There is no runtime data")
        ctx.instance.runtime_properties['data'] = current_data
        ctx.instance.update()
        if datetime.now() >= end_time:
            return
        sleep(1)
