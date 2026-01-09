#!/usr/bin/env python3
"""
Anthrobot Morphology MCP Server
================================

Visual vocabulary for Michael Levin's anthrobots - synthetic biological organisms
self-assembled from adult human tracheal cells.

Based on research by Gizem Gumuskaya et al., Advanced Science (2023, 2025).

Three-layer Lushy architecture:
- Layer 1: Categorical morphological taxonomy (YAML olog)
- Layer 2: Intentionality via morphospace navigation principles
- Layer 3: MCP server visual parameter generation (this file)
"""

from fastmcp import FastMCP
from typing import Dict, List, Optional, Any
from pathlib import Path
import yaml
import json

# Initialize FastMCP server
mcp = FastMCP("anthrobot-morphology")

# Load olog taxonomy
_olog_path = Path(__file__).parent / "anthrobot_morphology.olog.yaml"
with open(_olog_path) as f:
    OLOG = yaml.safe_load(f)


# ==============================================================================
# LAYER 1 - Pure Taxonomy Retrieval (Zero LLM Cost)
# ==============================================================================

@mcp.tool()
def list_morphotypes() -> str:
    """
    List all three anthrobot morphotypes with descriptions.
    
    Returns formatted overview of morphological categories from published research.
    """
    morphotypes = OLOG['types']
    
    result = "# Anthrobot Morphotypes (from Gumuskaya et al. 2023)\n\n"
    
    for key, data in morphotypes.items():
        result += f"## {data['name']}\n"
        result += f"**Type:** {key}\n"
        result += f"**Description:** {data['description']}\n\n"
    
    return result


@mcp.tool()
def get_movement_vocabulary() -> str:
    """
    Get complete taxonomy of anthrobot movement types.
    
    Returns movement classifications with morphological causes and visual signatures.
    """
    movements = OLOG['movement_types']
    
    result = "# Anthrobot Movement Vocabulary\n\n"
    result += "Movement emerges deterministically from morphology:\n\n"
    
    for movement_type, data in movements.items():
        result += f"## {movement_type.replace('_', ' ').title()}\n"
        result += f"**Morphological Cause:** {data['morphological_cause']}\n"
        result += f"**Speed:** {data['speed']}\n"
        result += f"**Trajectory:** {data['trajectory']}\n"
        result += f"**Visual Signature:** {data['visual_signature']}\n"
        result += f"**Intentionality:** {data['intentionality']}\n\n"
    
    return result


@mcp.tool()
def get_life_cycle_stages() -> str:
    """
    Get complete temporal progression through anthrobot life cycle.
    
    Returns all developmental stages from progenitor cell to senescence.
    """
    stages = OLOG['life_stages']
    
    result = "# Anthrobot Life Cycle (45-60 day lifespan)\n\n"
    
    for stage_key, data in stages.items():
        result += f"## {stage_key.replace('_', ' ').title()}\n"
        result += f"**Timepoint:** {data['timepoint']}\n"
        result += f"**Morphology:** {data['morphology']}\n"
        result += f"**Visual:** {data['visual']}\n"
        
        if 'gene_expression' in data:
            result += f"**Gene Expression:** {data['gene_expression']}\n"
        if 'event' in data:
            result += f"**Key Event:** {data['event']}\n"
        if 'epigenetic_state' in data:
            result += f"**Epigenetic State:** {data['epigenetic_state']}\n"
        if 'behavior' in data:
            result += f"**Behavior:** {data['behavior']}\n"
        if 'fate' in data:
            result += f"**Fate:** {data['fate']}\n"
        
        result += "\n"
    
    return result


@mcp.tool()
def get_imaging_aesthetics() -> str:
    """
    Get fluorescence microscopy imaging specifications and color palettes.
    
    Returns complete imaging modality vocabulary including channel assignments.
    """
    imaging = OLOG['imaging_modalities']
    
    result = "# Anthrobot Imaging Aesthetics\n\n"
    
    # Fluorescence multichannel
    fluor = imaging['fluorescence_multichannel']
    result += f"## {fluor['description']}\n\n"
    
    result += "### Fluorescence Channels:\n\n"
    for channel_name, channel_data in fluor['channels'].items():
        result += f"**{channel_name.replace('_', ' ').title()}**\n"
        result += f"- Stain: {channel_data['stain']}\n"
        result += f"- Color: {channel_data['color']}\n"
        result += f"- Targets: {channel_data['targets']}\n"
        result += f"- Visual Effect: {channel_data['visual_effect']}\n\n"
    
    result += f"### Composite Aesthetic:\n"
    composite = fluor['composite_aesthetic']
    result += f"- Corona Effect: {composite['corona_effect']}\n"
    result += f"- Depth Perception: {composite['depth_perception']}\n"
    result += f"- Color Harmony: {composite['color_harmony']}\n\n"
    
    # Other modalities
    result += f"## Depth Coloring\n"
    depth = imaging['depth_coloring']
    result += f"**Description:** {depth['description']}\n"
    result += f"**Visual Effect:** {depth['visual_effect']}\n"
    result += f"**Aesthetic:** {depth['aesthetic']}\n\n"
    
    result += f"## Brightfield Microscopy\n"
    bright = imaging['brightfield_microscopy']
    result += f"**Description:** {bright['description']}\n"
    result += f"**Visual Effect:** {bright['visual_effect']}\n"
    result += f"**Aesthetic:** {bright['aesthetic']}\n"
    
    return result


@mcp.tool()
def get_scale_references() -> str:
    """
    Get scale context for anthrobot size visualization.
    
    Critical for human understanding of micrometer scale objects.
    """
    scale = OLOG['scale_references']
    
    result = "# Anthrobot Scale Context\n\n"
    
    cellular = scale['cellular_scale']
    result += f"## Cellular Scale Context\n"
    result += f"**Anthrobot Size Range:** {cellular['anthrobot_size']}\n\n"
    result += "**Comparisons:**\n"
    for comp in cellular['comparison']:
        result += f"- {comp}\n"
    result += f"\n**Visual Niche:** {cellular['visual_niche']}\n\n"
    
    relative = scale['relative_to_source']
    result += f"## Relative to Source Cells\n"
    result += f"- Single tracheal cell: {relative['single_cell']}\n"
    result += f"- Mature anthrobot: {relative['mature_bot']}\n"
    result += f"- Scaling factor: {relative['scaling_factor']}\n"
    
    return result


@mcp.tool()
def get_intentionality_principles() -> str:
    """
    Get core intentionality explaining why anthrobot aesthetics work.
    
    Returns Levin's morphospace framework and physical/biological principles.
    """
    intent = OLOG['intentionality']
    
    result = "# Anthrobot Intentionality Principles\n\n"
    
    result += f"## Core Principle: {intent['core_principle']['concept']}\n"
    result += f"{intent['core_principle']['explanation']}\n\n"
    
    result += f"### Levin Framework:\n{intent['core_principle']['levin_framework']}\n\n"
    
    # Individual principles
    principles = [
        ('symmetry_determines_motion', 'Symmetry Determines Motion'),
        ('self_assembly_emergence', 'Self-Assembly Emergence'),
        ('age_reversal_paradox', 'Age Reversal Paradox'),
        ('wound_healing_mechanism', 'Wound Healing Mechanism'),
        ('cilia_as_computational_element', 'Cilia as Computational Element')
    ]
    
    for key, title in principles:
        data = intent[key]
        result += f"## {title}\n"
        result += f"**Principle:** {data['principle']}\n"
        
        for field in ['physics', 'mechanism', 'discovery', 'hypothesis']:
            if field in data:
                result += f"**{field.title()}:** {data[field]}\n"
        
        if 'visual_consequence' in data:
            result += f"**Visual Consequence:** {data['visual_consequence']}\n"
        if 'visual_signature' in data:
            result += f"**Visual Signature:** {data['visual_signature']}\n"
        if 'gene_expression' in data:
            result += f"**Gene Expression:** {data['gene_expression']}\n"
        if 'philosophical_implication' in data:
            result += f"**Philosophical Implication:** {data['philosophical_implication']}\n"
        
        result += "\n"
    
    return result


# ==============================================================================
# LAYER 2 - Deterministic Morphism Application (Zero LLM Cost)
# ==============================================================================

@mcp.tool()
def map_morphology_to_behavior(
    shape: str,
    cilia_pattern: str
) -> Dict[str, Any]:
    """
    Deterministic mapping from morphology to movement behavior.
    
    Pure Layer 2 morphism - no LLM calls, pure taxonomy lookup.
    
    Args:
        shape: "spherical", "potato_shaped", or "ellipsoidal"
        cilia_pattern: "fully_ciliated", "polar_clustered", or "dispersed_patches"
    
    Returns:
        Movement type, speed, trajectory, and physical explanation
    """
    morphisms = OLOG['morphisms']['shape_to_movement']['mappings']
    
    # Determine movement type from shape + cilia combination
    movement_data = None
    
    if shape == "spherical" and cilia_pattern == "fully_ciliated":
        movement_data = morphisms['spherical_symmetric']
    elif shape == "potato_shaped" and cilia_pattern == "polar_clustered":
        movement_data = morphisms['asymmetric_compact']
    elif shape == "ellipsoidal" and cilia_pattern == "dispersed_patches":
        movement_data = morphisms['elongated_balanced']
    
    if not movement_data:
        return {
            "error": "No exact mapping found",
            "suggestion": "Try: spherical+fully_ciliated, potato_shaped+polar_clustered, or ellipsoidal+dispersed_patches",
            "input_shape": shape,
            "input_cilia": cilia_pattern
        }
    
    # Get detailed movement info
    movement_type = movement_data['movement']
    movement_details = OLOG['movement_types'][movement_type]
    
    return {
        "shape": movement_data['shape'],
        "cilia_pattern": movement_data['cilia'],
        "movement_type": movement_type,
        "speed": movement_details['speed'],
        "trajectory": movement_details['trajectory'],
        "visual_signature": movement_details['visual_signature'],
        "physical_reason": movement_data['reason'],
        "morphological_cause": movement_details['morphological_cause'],
        "intentionality": movement_details['intentionality']
    }


@mcp.tool()
def get_morphotype_specifications(morphotype: str) -> Dict[str, Any]:
    """
    Get complete visual specifications for a morphotype.
    
    Layer 2 deterministic assembly from taxonomy.
    
    Args:
        morphotype: "morphotype_1", "morphotype_2", or "morphotype_3"
    
    Returns:
        Complete morphotype specifications including visual parameters
    """
    if morphotype not in OLOG['types']:
        return {"error": f"Unknown morphotype: {morphotype}. Use morphotype_1, morphotype_2, or morphotype_3"}
    
    # Base type info
    type_data = OLOG['types'][morphotype]
    
    # Get visual parameters
    visual_params = OLOG['visual_parameters']['morphotype_to_silhouette'].get(morphotype, {})
    
    # Get associated movement
    movements = OLOG['movement_types']
    associated_movement = None
    
    if morphotype == "morphotype_1":
        associated_movement = movements['stationary_wiggler']
    elif morphotype == "morphotype_2":
        associated_movement = movements['circular_swimmer']
    elif morphotype == "morphotype_3":
        associated_movement = movements['straight_swimmer']
    
    return {
        "morphotype": morphotype,
        "name": type_data['name'],
        "description": type_data['description'],
        "silhouette": visual_params,
        "typical_movement": associated_movement,
        "visual_identity": f"{type_data['name']} - {type_data['description']}"
    }


@mcp.tool()
def calculate_size_effects(size_micrometers: float) -> Dict[str, Any]:
    """
    Determine behavioral tendencies based on anthrobot size.
    
    Layer 2 deterministic mapping.
    
    Args:
        size_micrometers: Size in micrometers (30-500)
    
    Returns:
        Size category, behavioral tendencies, and physical reasoning
    """
    size_mappings = OLOG['morphisms']['size_to_behavior']['mappings']
    
    if size_micrometers < 30 or size_micrometers > 500:
        return {
            "warning": "Size outside observed range",
            "valid_range": "30-500 micrometers",
            "input_size": size_micrometers
        }
    
    if size_micrometers <= 100:
        category = size_mappings['small_bots']
        cat_name = "small"
    elif size_micrometers <= 300:
        category = size_mappings['medium_bots']
        cat_name = "medium"
    else:
        category = size_mappings['large_bots']
        cat_name = "large"
    
    # Get scale reference
    scale_refs = OLOG['scale_references']['cellular_scale']['comparison']
    reference = "Between red blood cell and Paramecium"
    
    if size_micrometers < 70:
        reference = "Smaller than human hair diameter (~70µm)"
    elif size_micrometers < 100:
        reference = "About human hair thickness"
    elif size_micrometers < 300:
        reference = "2-4x human hair thickness"
    else:
        reference = "Visible as small dot to naked eye"
    
    return {
        "size_micrometers": size_micrometers,
        "size_category": cat_name,
        "size_range": category['size_range'],
        "behavioral_tendency": category['tendency'],
        "physical_reason": category['reason'],
        "scale_reference": reference,
        "visual_impact": f"At {size_micrometers}µm, appears {reference.lower()}"
    }


# ==============================================================================
# LAYER 3 - Visual Parameter Generation for Claude Synthesis
# ==============================================================================

@mcp.tool()
def generate_anthrobot_visualization(
    morphotype: str,
    size_micrometers: float = 150,
    life_stage: str = "mature",
    imaging_style: str = "scientific"
) -> Dict[str, Any]:
    """
    Generate complete visual parameters for an anthrobot.
    
    Layer 3 tool - assembles deterministic parameters for Claude synthesis.
    
    Args:
        morphotype: "morphotype_1", "morphotype_2", or "morphotype_3"
        size_micrometers: Size (30-500), default 150
        life_stage: "progenitor", "early_spheroid", "eversion", "mature", "senescent"
        imaging_style: "scientific", "artistic", or "depth_map"
    
    Returns:
        Complete visual parameter set ready for Claude synthesis
    """
    # Get morphotype specs
    morph_specs = get_morphotype_specifications(morphotype)
    if "error" in morph_specs:
        return morph_specs
    
    # Get size effects
    size_effects = calculate_size_effects(size_micrometers)
    
    # Get life stage info
    if life_stage not in OLOG['life_stages']:
        return {"error": f"Unknown life_stage: {life_stage}"}
    
    stage_data = OLOG['life_stages'][life_stage]
    
    # Get imaging parameters
    imaging_params = OLOG['visual_parameters']['imaging_style_palette'].get(imaging_style, {})
    
    # Assemble cilia rendering
    if morphotype == "morphotype_1":
        cilia_key = "fully_ciliated"
    elif morphotype == "morphotype_2":
        cilia_key = "polar_clustered"
    else:
        cilia_key = "dispersed_patches"
    
    cilia_rendering = OLOG['visual_parameters']['cilia_corona_rendering'][cilia_key]
    
    # Movement visualization
    if morphotype == "morphotype_1":
        movement_viz = "static_image"
    else:
        movement_viz = "trajectory_traces"
    
    movement_params = OLOG['visual_parameters']['movement_visualization'][movement_viz]
    
    return {
        "anthrobot_specifications": {
            "morphotype": morphotype,
            "name": morph_specs['name'],
            "size_micrometers": size_micrometers,
            "life_stage": life_stage
        },
        
        "silhouette_geometry": morph_specs['silhouette'],
        
        "cilia_corona": {
            "pattern": cilia_key,
            "rendering": cilia_rendering,
            "visual_identity": "Corona of motile cilia"
        },
        
        "movement_signature": {
            "type": morph_specs['typical_movement']['morphological_cause'],
            "speed": morph_specs['typical_movement']['speed'],
            "trajectory": morph_specs['typical_movement']['trajectory'],
            "visual_signature": morph_specs['typical_movement']['visual_signature'],
            "rendering": movement_params
        },
        
        "scale_context": {
            "size": size_micrometers,
            "category": size_effects['size_category'],
            "reference": size_effects['scale_reference'],
            "visual_impact": size_effects['visual_impact']
        },
        
        "life_stage_characteristics": {
            "stage": life_stage,
            "timepoint": stage_data['timepoint'],
            "morphology": stage_data['morphology'],
            "visual_appearance": stage_data['visual']
        },
        
        "imaging_aesthetics": {
            "style": imaging_style,
            "palette": imaging_params,
            "modality": "Fluorescence microscopy" if imaging_style == "scientific" else imaging_style
        },
        
        "synthesis_instructions": OLOG['synthesis_guidance']['for_claude_creative_synthesis']
    }


@mcp.tool()
def generate_life_cycle_sequence(
    morphotype: str,
    start_stage: str = "progenitor",
    end_stage: str = "mature",
    size_micrometers: float = 150
) -> Dict[str, Any]:
    """
    Generate temporal progression through anthrobot development.
    
    Layer 3 tool for time-lapse sequence parameters.
    
    Args:
        morphotype: Which morphotype to follow through development
        start_stage: Starting life stage (default "progenitor")
        end_stage: Ending life stage (default "mature")
        size_micrometers: Final mature size
    
    Returns:
        Sequence of stage parameters with transition events
    """
    # Stage order
    stage_order = [
        "progenitor_cell",
        "early_spheroid",
        "eversion",
        "mature_anthrobot",
        "senescence"
    ]
    
    # Map user input to full keys
    stage_mapping = {
        "progenitor": "progenitor_cell",
        "early_spheroid": "early_spheroid",
        "eversion": "eversion",
        "mature": "mature_anthrobot",
        "senescent": "senescence"
    }
    
    start_key = stage_mapping.get(start_stage, start_stage)
    end_key = stage_mapping.get(end_stage, end_stage)
    
    if start_key not in stage_order or end_key not in stage_order:
        return {"error": "Invalid stage names"}
    
    start_idx = stage_order.index(start_key)
    end_idx = stage_order.index(end_key)
    
    if start_idx > end_idx:
        return {"error": "Start stage must come before end stage"}
    
    # Build sequence
    sequence = []
    stages_data = OLOG['life_stages']
    
    for stage_key in stage_order[start_idx:end_idx+1]:
        stage_info = stages_data[stage_key]
        
        # Determine size for this stage
        if stage_key == "progenitor_cell":
            stage_size = 15
        elif stage_key == "early_spheroid":
            stage_size = size_micrometers * 0.3
        elif stage_key == "eversion":
            stage_size = size_micrometers * 0.6
        elif stage_key == "mature_anthrobot":
            stage_size = size_micrometers
        else:  # senescence
            stage_size = size_micrometers * 0.8
        
        sequence.append({
            "stage_name": stage_key,
            "timepoint": stage_info['timepoint'],
            "morphology": stage_info['morphology'],
            "visual_appearance": stage_info['visual'],
            "size_micrometers": stage_size,
            "gene_expression": stage_info.get('gene_expression', 'N/A'),
            "key_event": stage_info.get('event', stage_info.get('fate', 'Continued development'))
        })
    
    return {
        "morphotype": morphotype,
        "sequence_length": len(sequence),
        "total_timespan": f"{start_stage} to {end_stage}",
        "stages": sequence,
        "critical_transitions": [
            "Eversion (Day 0-3): Inside-out turning, cilia reorientation - DRAMATIC",
            "Maturation (Day 10): Stable motile form achieved",
            "Senescence (Day 45+): Natural biodegradation begins"
        ]
    }


@mcp.tool()
def simulate_swarm_behavior(
    bot_count: int = 5,
    morphotype_mix: Optional[Dict[str, float]] = None,
    behavior: str = "swimming",
    imaging_style: str = "scientific"
) -> Dict[str, Any]:
    """
    Generate parameters for multiple anthrobots in collective arrangement.
    
    Layer 3 complex scene synthesis.
    
    Args:
        bot_count: Number of anthrobots (3-20)
        morphotype_mix: Optional distribution like {"morphotype_1": 0.3, "morphotype_2": 0.4, "morphotype_3": 0.3}
        behavior: "swimming", "wound_seeking", or "bridge_formation"
        imaging_style: "scientific" or "artistic"
    
    Returns:
        Swarm composition with individual and collective parameters
    """
    if bot_count < 3 or bot_count > 20:
        return {"error": "bot_count must be 3-20"}
    
    # Default mix: equal distribution
    if morphotype_mix is None:
        morphotype_mix = {
            "morphotype_1": 0.33,
            "morphotype_2": 0.33,
            "morphotype_3": 0.34
        }
    
    # Calculate counts
    counts = {
        "morphotype_1": int(bot_count * morphotype_mix.get("morphotype_1", 0)),
        "morphotype_2": int(bot_count * morphotype_mix.get("morphotype_2", 0)),
        "morphotype_3": int(bot_count * morphotype_mix.get("morphotype_3", 0))
    }
    
    # Adjust for rounding
    total = sum(counts.values())
    if total < bot_count:
        counts["morphotype_1"] += (bot_count - total)
    
    # Generate individual bots
    bots = []
    bot_id = 1
    
    for morphotype, count in counts.items():
        for _ in range(count):
            size = 50 + (bot_id * 30) % 300  # Vary sizes 50-350µm
            
            bots.append({
                "bot_id": bot_id,
                "morphotype": morphotype,
                "size_micrometers": size,
                "specs": get_morphotype_specifications(morphotype)
            })
            
            bot_id += 1
    
    # Spatial arrangement based on behavior
    if behavior == "swimming":
        arrangement = {
            "type": "dispersed",
            "description": "Bots distributed naturally with varied orientations",
            "spacing": "50-200 micrometers between individuals"
        }
    elif behavior == "wound_seeking":
        arrangement = {
            "type": "converging",
            "description": "Bots oriented toward central wound/scratch",
            "spacing": "Decreasing density toward wound edge"
        }
    elif behavior == "bridge_formation":
        arrangement = {
            "type": "linear_chain",
            "description": "Bots aligned in bridge across gap",
            "spacing": "End-to-end contact, minimal gaps"
        }
    else:
        arrangement = {"type": "random"}
    
    # Collective behavior description
    behaviors_data = OLOG.get('behaviors', {})
    behavior_desc = behaviors_data.get(behavior.replace('_', ''), {})
    
    return {
        "swarm_composition": {
            "total_bots": bot_count,
            "morphotype_distribution": counts,
            "size_range": f"{min(b['size_micrometers'] for b in bots):.0f}-{max(b['size_micrometers'] for b in bots):.0f} µm"
        },
        
        "individual_bots": bots,
        
        "spatial_arrangement": arrangement,
        
        "collective_behavior": {
            "behavior_type": behavior,
            "description": behavior_desc.get('description', f'{behavior} behavior'),
            "visual_signature": behavior_desc.get('visual_signature', 'Multiple anthrobots in coordinated activity'),
            "scale": behavior_desc.get('scalability', 'Scalable from individual to thousands')
        },
        
        "imaging_parameters": {
            "style": imaging_style,
            "frame_composition": "Wide field showing multiple subjects",
            "depth_of_field": "Moderate - some bots in focus, others contextual blur",
            "visual_complexity": "High - multiple subjects with individual characteristics"
        },
        
        "synthesis_note": f"Swarm of {bot_count} anthrobots engaged in {behavior} - emphasize both individual morphologies and collective pattern"
    }


@mcp.tool()
def get_wound_healing_scenario() -> Dict[str, Any]:
    """
    Get complete parameters for wound healing bridge formation scenario.
    
    This is one of the most visually striking anthrobot behaviors.
    
    Returns:
        Multi-frame sequence showing wound repair process
    """
    return {
        "scenario_name": "Wound Healing Bridge Formation",
        
        "scientific_context": {
            "discovery": "Anthrobots spontaneously form bridges across neural damage",
            "mechanism": "Unknown - possibly bioelectric sensing or chemotaxis",
            "healing_effect": "Neural regrowth occurs across anthrobot bridge",
            "significance": "Demonstrates therapeutic potential for personalized medicine"
        },
        
        "visual_sequence": [
            {
                "frame": 1,
                "timepoint": "T=0 (Initial state)",
                "description": "Scratch/tear in red neural cell layer",
                "gap_width": "100-300 micrometers",
                "anthrobot_positions": "Scattered around wound periphery",
                "anthrobot_count": 5,
                "visual_notes": "Anthrobots randomly oriented, not yet wound-seeking"
            },
            {
                "frame": 2,
                "timepoint": "T=30 minutes",
                "description": "Anthrobots migrating toward wound",
                "gap_width": "100-300 micrometers (unchanged)",
                "anthrobot_positions": "Moving into gap, beginning to align",
                "visual_notes": "Yellow cilia coronas visible, trajectory traces showing convergence",
                "emergent_behavior": "Collective wound-seeking initiated"
            },
            {
                "frame": 3,
                "timepoint": "T=2 hours",
                "description": "Bridge formation complete",
                "gap_width": "100-300 micrometers (spanned)",
                "anthrobot_positions": "Linear chain spanning gap end-to-end",
                "visual_notes": "Anthrobots in contact, forming continuous bridge",
                "healing_evidence": "Green neural regrowth visible crossing bridge"
            },
            {
                "frame": 4,
                "timepoint": "T=24-48 hours",
                "description": "Tissue reconnection",
                "gap_width": "Partially closed",
                "neural_regrowth": "Complete reconnection across former gap",
                "anthrobot_state": "Still present or beginning to disperse",
                "outcome": "Functional neural repair achieved"
            }
        ],
        
        "imaging_specifications": {
            "neural_layer_stain": "Red (tight junctions or cell tracker)",
            "anthrobot_cilia": "Yellow (acetylated tubulin)",
            "neural_regrowth": "Green (growth marker)",
            "background": "Black (fluorescence standard)",
            "time_lapse_interval": "5-15 minutes per frame"
        },
        
        "visual_drama": {
            "key_moment": "Frame 3 - complete bridge spans gap",
            "aesthetic_principle": "Ant bridge structure - living scaffolding",
            "emotional_impact": "Adult cells collaborating to heal damage",
            "scale_wonder": "Microscopic repair with macro-scale implications"
        },
        
        "synthesis_guidance": """
        This is the 'hero shot' of anthrobot research. Emphasize:
        1. The GAP - make the wound/injury visually clear
        2. The MIGRATION - show directional movement toward damage
        3. The BRIDGE - linear chain formation is stunning
        4. The HEALING - green regrowth crossing the bridge
        5. The SCALE - this happens at cellular scale but has huge implications
        
        Visual metaphor: Cellular emergency response team building living bridge.
        """
    }


# ==============================================================================
# Cross-Domain Composition Tools
# ==============================================================================

@mcp.tool()
def suggest_composition_domains() -> str:
    """
    Suggest other Lushy domains that compose well with anthrobot morphology.
    
    Returns recommendations for categorical composition.
    """
    compositions = OLOG.get('composition_targets', {})
    
    result = "# Composition Opportunities for Anthrobot Morphology\n\n"
    
    for domain_name, data in compositions.items():
        result += f"## {domain_name.replace('_', ' ').title()}\n"
        
        result += "**Shared Structure:**\n"
        for struct in data['shared_structure']:
            result += f"- {struct}\n"
        
        if 'natural_transformation' in data:
            trans = data['natural_transformation']
            result += f"\n**Natural Transformation:**\n"
            result += f"- Source: {trans['source']}\n"
            result += f"- Target: {trans['target']}\n"
            result += "- Component mappings:\n"
            for comp_name, comp_val in trans['components'].items():
                result += f"  - {comp_name}: {comp_val}\n"
        
        if 'conceptual_bridge' in data:
            bridge = data['conceptual_bridge']
            result += f"\n**Conceptual Bridge:**\n"
            for concept, mapping in bridge.items():
                result += f"- {concept}: {mapping}\n"
        
        if 'functional_mapping' in data:
            fmap = data['functional_mapping']
            result += f"\n**Functional Mapping:**\n"
            for func, target in fmap.items():
                result += f"- {func}: {target}\n"
        
        result += "\n"
    
    return result


@mcp.tool()
def get_research_attribution() -> str:
    """
    Get complete research citations and educational resources.
    
    Returns attribution to Levin Lab and links to primary sources.
    """
    citations = OLOG.get('citations', {})
    
    result = "# Anthrobot Research Attribution\n\n"
    
    result += "## Primary Research Papers\n\n"
    result += f"### Original Discovery (2023)\n{citations.get('primary_source', '')}\n\n"
    result += f"### Life Cycle Study (2025)\n{citations.get('life_cycle_source', '')}\n\n"
    result += f"### Philosophical Framework\n{citations.get('levin_philosophy', '')}\n\n"
    
    if 'educational_gateway' in citations:
        gateway = citations['educational_gateway']
        result += f"## Educational Resources\n\n"
        result += f"{gateway['description']}\n\n"
        result += "**Links:**\n"
        for link in gateway.get('links', []):
            result += f"- {link}\n"
    
    result += "\n## Research Team\n"
    result += "- **Michael Levin, PhD** - Director, Allen Discovery Center at Tufts\n"
    result += "- **Gizem Gumuskaya** - Lead researcher\n"
    result += "- **Tufts University** - Allen Discovery Center\n\n"
    
    result += "## Key Concepts from Levin Lab\n"
    result += "- Morphological computation\n"
    result += "- Bioelectric signaling in development\n"
    result += "- Synthetic morphology as research platform\n"
    result += "- Platonic morphospace navigation\n"
    result += "- Regenerative medicine applications\n"
    
    return result


# Entry point for FastMCP
if __name__ == "__main__":
    mcp.run()
