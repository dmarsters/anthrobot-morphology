# Anthrobot Morphology MCP Server

**Visual vocabulary for Michael Levin's anthrobots** - synthetic biological organisms self-assembled from adult human tracheal cells.

Part of the [Lushy](https://lushy.app) epistemological infrastructure platform for translating domain expertise into visual parameters.

## 🧬 What are Anthrobots?

Anthrobots are living biobots that spontaneously self-assemble from adult human tracheal cells into novel multicellular forms with distinct morphologies and behaviors. Discovered by the [Levin Lab at Tufts University](https://drmichaellevin.org), they demonstrate that adult cells can reorganize into forms beyond their evolutionary defaults.

**Key characteristics:**
- Self-assemble from single cells (no genetic editing required)
- Develop motile cilia for swimming
- Seek out and repair neural damage
- Form "bridges" across wounds to enable healing
- Biologically younger than source cells (epigenetic age reversal!)
- Lifespan: 45-60 days before natural biodegradation

## 🎯 Purpose

This MCP server provides a complete visual vocabulary for generating images of anthrobots with categorical precision. It translates research-based morphological taxonomy into image generation parameters while preserving the scientific accuracy and wonder of this biological innovation.

### Three-Layer Lushy Architecture

1. **Layer 1 (Foundation)**: Categorical morphological taxonomy from published research
2. **Layer 2 (Structure)**: Intentionality via morphospace navigation principles 
3. **Layer 3 (Synthesis)**: Parameter assembly for AI image generation

**Cost profile**: Layers 1-2 are deterministic (0 LLM tokens). Only Layer 3 synthesis requires LLM.

## 🛠️ Available Tools

### Layer 1: Pure Taxonomy (0 tokens)

#### `list_morphotypes()`
Get all three anthrobot morphotypes with descriptions.

```python
# Returns: Morphotype 1 (Spherical Wiggler), 2 (Asymmetric Circler), 3 (Ellipsoidal Swimmer)
```

#### `get_movement_vocabulary()`
Complete taxonomy of movement types with morphological causes.

#### `get_life_cycle_stages()`
Temporal progression from progenitor cell → senescence (45-60 days).

#### `get_imaging_aesthetics()`
Fluorescence microscopy specifications and color palettes.

#### `get_scale_references()`
Scale context for visualizing micrometer-scale objects.

#### `get_intentionality_principles()`
Core principles explaining why anthrobot aesthetics work.

### Layer 2: Deterministic Morphisms (0 tokens)

#### `map_morphology_to_behavior(shape, cilia_pattern)`
Deterministic mapping: morphology → movement type.

```python
# Example: spherical + fully_ciliated → stationary_wiggler
# Reason: "Forces cancel due to radial symmetry"
```

#### `get_morphotype_specifications(morphotype)`
Complete specifications for morphotype_1, morphotype_2, or morphotype_3.

#### `calculate_size_effects(size_micrometers)`
Behavioral tendencies based on size (30-500µm range).

### Layer 3: Visual Parameter Generation

#### `generate_anthrobot_visualization(morphotype, size_micrometers, life_stage, imaging_style)`
Generate complete visual parameters for image generation.

**Args:**
- `morphotype`: "morphotype_1", "morphotype_2", or "morphotype_3"
- `size_micrometers`: 30-500 (default 150)
- `life_stage`: "progenitor", "early_spheroid", "eversion", "mature", "senescent"
- `imaging_style`: "scientific", "artistic", or "depth_map"

**Returns:**
```json
{
  "anthrobot_specifications": {...},
  "silhouette_geometry": {...},
  "cilia_corona": {...},
  "movement_signature": {...},
  "scale_context": {...},
  "imaging_aesthetics": {...},
  "synthesis_instructions": "..."
}
```

#### `generate_life_cycle_sequence(morphotype, start_stage, end_stage)`
Temporal progression sequence for time-lapse visualization.

#### `simulate_swarm_behavior(bot_count, morphotype_mix, behavior)`
Multi-anthrobot scene parameters.

**Behaviors:**
- `"swimming"`: Dispersed natural swimming
- `"wound_seeking"`: Converging toward damage
- `"bridge_formation"`: Linear chain across gap

#### `get_wound_healing_scenario()`
Complete multi-frame wound repair sequence - the "hero shot" of anthrobot research.

### Cross-Domain Tools

#### `suggest_composition_domains()`
Recommend other Lushy domains for categorical composition.

#### `get_research_attribution()`
Complete citations and educational resources.

## 🎨 Example Workflows

### Basic Visualization

```
User: "Generate a mature anthrobot with a ciliated corona"

LLM calls: generate_anthrobot_visualization(
    morphotype="morphotype_1",
    size_micrometers=150,
    life_stage="mature",
    imaging_style="scientific"
)

Result: Spherical anthrobot, 150µm (2x hair thickness), complete yellow 
cilia corona creating bioluminescent halo. Blue DAPI-stained nuclei core 
(~20 cells visible). Scientific fluorescence aesthetic - sharp, publishable 
quality. Slight shimmer blur indicating ciliary motion but minimal displacement 
(wiggler behavior due to radial symmetry).
```

### Wound Healing Sequence

```
User: "Show anthrobots healing a wound"

LLM calls: get_wound_healing_scenario()

Result: 4-frame temporal sequence:
Frame 1 (T=0): Red neural layer with vertical scratch, 5 anthrobots scattered
Frame 2 (T=30min): Bots migrating into gap, yellow cilia trails visible
Frame 3 (T=2hr): Complete bridge - 5 bots in linear chain spanning gap
Frame 4 (T=24-48hr): Green neural regrowth crossing the living bridge

Visual metaphor: Cellular emergency response building living scaffolding.
```

### Swarm Composition

```
User: "Create a swarm of different sized anthrobots"

LLM calls: simulate_swarm_behavior(
    bot_count=7,
    morphotype_mix={"morphotype_1": 0.3, "morphotype_2": 0.4, "morphotype_3": 0.3},
    behavior="swimming"
)

Result: 7 anthrobots - mix of spherical wigglers, asymmetric circlers, and 
straight swimmers. Size range 80-320µm for visual diversity. Dispersed natural 
arrangement, some in sharp focus, others contextually blurred for depth. Each 
with characteristic corona pattern and movement blur signature.
```

## 🔬 Research Attribution

### Primary Research Papers

**Original Discovery (2023)**  
Gumuskaya, G., Srivastava, P., Cooper, B.G., Lesser, H., Semegran, B., Garnier, S., and Levin, M. (2023). "Motile Living Biobots Self-Construct from Adult Human Somatic Progenitor Seed Cells." *Advanced Science*. doi: 10.1002/advs.202303575

**Life Cycle Study (2025)**  
Gumuskaya, G., Davey, N., Srivastava, P., Bender, A., Pio-Lopez, L., Hazel, D., and Levin, M. (2025). "The Morphological, Behavioral, and Transcriptomic Life Cycle of Anthrobots." *Advanced Science*. doi: 10.1002/advs.202409330

### Research Team

- **Michael Levin, PhD** - Director, Allen Discovery Center at Tufts
- **Gizem Gumuskaya** - Lead researcher
- **Tufts University** - Allen Discovery Center

### Educational Resources

- [Michael Levin Lab](https://drmichaellevin.org)
- [Levin's Blog: Thoughtforms.life](https://thoughtforms.life)
- Tufts University Allen Discovery Center

## 🧠 Intentionality Principles

### Morphological Attractor States

> Adult cells, freed from tissue-level constraints, navigate morphospace toward stable forms determined by physical forces, bioelectric patterns, and collective cell intelligence - not genetic programming alone.

**Levin's Framework:** Cells are problem-solving agents navigating toward "target morphologies" from a Platonic space of possible forms. The genome provides hardware (receptors, channels, enzymes), while emergent bioelectric/biomechanical forces provide the software.

### Key Principles

**Symmetry Determines Motion**  
At low Reynolds number (Re < 0.1), radially symmetric cilia beating produces forces that cancel out. Asymmetry is REQUIRED for displacement.

**Self-Assembly Emergence**  
No external sculpting, no genetic editing. Cells aggregate based on adhesion molecules, bioelectric signaling, mechanical forces, and collective intelligence.

**Age Reversal Paradox**  
Mature anthrobots show younger epigenetic age than source adult cells. Reorganizing into new morphology RESETS cellular aging markers!

**Wound Healing Mechanism**  
Anthrobots spontaneously seek damaged tissue, form bridges across gaps, and induce neural regrowth. Mechanism unknown but likely involves bioelectric signaling.

**Cilia as Computation**  
Each cilium is mechanosensitive AND motile. Corona "shimmer" represents real-time distributed computation - emergent pattern without central control.

## 🎯 Composition Potential

This domain composes naturally with:

- **Microscopy Aesthetics**: Fluorescence imaging, Z-stack rendering, scale relationships
- **Temporal Progression**: Developmental sequences, morphogenetic transitions
- **Emergence Patterns**: Self-assembly dynamics, attractor states, bottom-up organization
- **Healing/Repair**: Wound response, regenerative scaffolding, tissue reconnection

## 📊 Cost Profile

| Layer | Operation | LLM Tokens | Cost |
|-------|-----------|------------|------|
| Layer 1 | Taxonomy retrieval | 0 | $0.00 |
| Layer 2 | Morphism application | 0 | $0.00 |
| Layer 3 | Parameter assembly | 0 | $0.00 |
| Synthesis | LLM creative synthesis | ~500-1500 | ~$0.01 |

**Cognitive leverage**: Expert knowledge compressed into deterministic mappings, enabling reproducible intention transfer at minimal cost.

## 🧪 Development

```bash
# Run tests
pytest test_anthrobot_server.py -v

# Expected: 40+ tests covering all tools
# All tests use deterministic lookups (no mocks needed)
```

## 📄 License

MIT License - see LICENSE file

## 🙏 Acknowledgments

This MCP server translates the groundbreaking research of the Levin Lab into accessible visual vocabulary. The work represents profound insights into cellular plasticity, morphological computation, and synthetic biology.

**Please cite the original research papers if using this tool for scientific visualization or communication.**

## 🔗 Links

- [Lushy Platform](https://lushy.app)
- [Levin Lab](https://drmichaellevin.org)
- [FastMCP](https://github.com/jlowin/fastmcp)
- [MCP Protocol](https://modelcontextprotocol.io)

---

**Built with the Lushy three-layer olog methodology**: Categorical structure → Intentionality reasoning → MCP implementation
