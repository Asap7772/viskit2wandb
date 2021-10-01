from core import *
import wandb

if __name__ == '__main__':
    dirs = ['/home/asap7772/asap7772/bc-vs-offlinerl/data']
    wandb_out = 'bc_v_cql'

    for dir in dirs:
        print(dir)
    
    exps_data = load_exps_data(dirs)
    plottable_keys = list(
        set(flatten(list(exp.progress.keys()) for exp in exps_data)))
    plottable_keys = sorted([k for k in plottable_keys if k is not None])
    distinct_params = sorted(extract_distinct_params(exps_data))

    print(plottable_keys)
    print(distinct_params)

    for exp in exps_data:
        wandb.init(project=wandb_out, config = exp['params'], reinit=True)
        lst = [{key: exp.progress[key][i] for key in exp.progress} for i in range(len(exp.progress['Epoch']))]
        print(len(lst))
        for c, x in enumerate(lst):
            wandb.log(x, step=c)
