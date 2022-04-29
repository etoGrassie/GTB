from random import choice


class GTBProceed(object):

    def proceed_task(self, task_line=''):
        random_list = []
        task = self.format_task(task_line)
        if bool(task) is False:
            return
        try:
            task = task.split(' ')
        except AttributeError:
            return AttributeError
        finally:
            pass

        length = len(task)
        if length < 2:
            return ValueError
        if task[0] != 'task' or 'TSK' or '::' not in task[0]:
            return ValueError
        try:
            if task[1] == 'random' or 'RAND':
                if task[2] == 'number' or 'NUM':
                    if bool(random_list) is False:
                        random_list = list(range(int(task[3]), int(task[4])))
                    random_num = choice(random_list)
                    random_list.remove(random_num)
                    return {task, str(random_num)}
                elif task[2] == 'object' or 'OBJ':
                    if bool(random_list) is False:
                        random_list = task[3].split('&&')
                    random_object = choice(random_list)
                    return random_object

            elif '::' in task[0]:
                return_multiple_successful = []
                multiple = task[0].replace('::', '')
                multiple_times = int(multiple)
                if multiple_times >= 2:
                    current_time = 0
                    while current_time < multiple_times:
                        try:
                            if task[2] == 'random' or 'RAND':
                                if task[3] == 'number' or 'NUM':
                                    if bool(random_list) is False:
                                        random_list = list(range(int(task[4]), int(task[5])))
                                    random_num = choice(random_list)
                                    random_list.remove(random_num)
                                    return_multiple_successful.append(str(random_num))
                                elif task[3] == 'object' or 'OBJ':
                                    if bool(random_list) is False:
                                        random_list = task[4].split('&&')
                                    random_object = choice(random_list)
                                    return random_object

                        except (IndexError, AttributeError, ValueError) as ex:
                            return ex
                            break
                        finally:
                            pass
                        current_time += 1
                    return return_multiple_successful
                else:
                    return ValueError
            else:
                return ValueError
        except (IndexError, AttributeError, ValueError) as ex:
            return ex

    def proceed_multiple_tasks(self, tasks=[]):
        return_successful = []
        return_failed = {}
        index = [1]
        for task, index_ in zip(tasks, index):
            proceed_result = self.proceed_task(task)
            if proceed_result != IndexError or AttributeError or ValueError:
                return_successful.append(proceed_result)
            elif proceed_result == IndexError:
                return_failed[str(index_) + ' - ' + task] = 'IndexError'
            elif proceed_result == ValueError:
                return_failed[str(index_) + ' - ' + task] = 'ValueError'
            elif proceed_result == AttributeError:
                return_failed[str(index_) + ' - ' + task] = 'AttributeError'
        index.append(index_ + 1)
        return {'successfully': return_successful, 'failed': return_failed}

    @staticmethod
    def format_task(task):
        task = task.replace(' ', '')
        task = task.replace('\n', '')
        task = task.replace('\t', '')
        return task
