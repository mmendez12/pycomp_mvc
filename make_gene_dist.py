__author__ = 'mickael'

__author__ = 'mickael'

from pycomp_mvc import extra

from pycomp_mvc.controller import genes

if __name__ == '__main__':
    cfg, gac = extra.load_configs('/home/mickael/Projects/pycomp_mvc_test/input/global_config_ac2.yaml',
                                  '/home/mickael/Projects/pycomp_mvc_test/input/2015-04-02_f5_primary-cell_CL_comparisons_libid.yml')

    dataset = [dataset for dataset in cfg['datasets'] if dataset['name'] == 'lncRNA_intergenic_antisense'][0]
    genes.gene_dist(cfg, gac, dataset, 'lncRNA_genic_antisense|d_lncRNA|CATG00000107175.1')