import logging

from scout.models.phenotype_term import HpoTerm

LOG = logging.getLogger(__name__)

def build_hpo_term(hpo_info):
    """Build a hpo_term object
    
    Check that the information is correct and add the correct hgnc ids to the 
    array of genes.
    
        Args:
            hpo_info(dict)
        
        Returns:
            hpo_obj(scout.models.HpoTerm): A dictionary with hpo information
    
    """
    
    try:
        hpo_id = hpo_info['hpo_id']
    except KeyError:
        raise KeyError("Hpo terms has to have a hpo_id")

    LOG.debug("Building hpo term %s", hpo_id)

    # Add description to HPO term
    try:
        description = hpo_info['description']
    except KeyError:
        raise KeyError("Hpo terms has to have a description")

    hpo_obj = HpoTerm(
        hpo_id = hpo_id,
        description = description
    )
    
    # Add links to hgnc genes if any
    hgnc_ids = hpo_info.get('genes', set())
    if hgnc_ids:
        hpo_obj['genes'] = list(hgnc_ids)
    
    return hpo_obj

