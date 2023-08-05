from typing import Final

from .define import Building, Item, Ingredients, Liquid
from .sf_calc import Recipe, RecipeIO


def alternate(product: Item, num: int = 1) -> str:
    """代替レシピのキーを生成する

    Args:
        product: 生成されるアイテム名
        num: 代替レシピの番号 ( n番目 )

    Returns:
        キー
    """
    return f"alternate{num}_{product}"


def byproduct(product: Item, num: int = 1) -> str:
    """副産物からレシピを探すためのサブキーを生成する

    Args:
        product: 生成される副産物のアイテム
        num: 副産物レシピの番号 ( n番目 )

    Returns:
        キー
    """
    return f"byproduct{num}_{product}"


RECIPE: Final[dict[str | Item, Recipe]] = {
                                                                                                                                                                # Limestone
    Ingredients.limestone:
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.limestone, 240),
        Building.miner_mk3,
    ),
    Ingredients.concrete:
    Recipe(
        RecipeIO(Ingredients.limestone, 45),
        RecipeIO(Ingredients.concrete, 15),
        Building.smelter,
    ),
                                                                                                                                                                # Iron
    Ingredients.iron_ore:
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.iron_ore, 240),
        Building.miner_mk3,
    ),
    Ingredients.iron_ingot:
    Recipe(
        RecipeIO(Ingredients.iron_ore, 30),
        RecipeIO(Ingredients.iron_ingot, 30),
        Building.smelter,
    ),
    Ingredients.iron_plate:
    Recipe(
        RecipeIO(Ingredients.iron_ingot, 30),
        RecipeIO(Ingredients.iron_plate, 20),
        Building.constructor,
    ),
    Ingredients.iron_rod:
    Recipe(
        RecipeIO(Ingredients.iron_ingot, 15),
        RecipeIO(Ingredients.iron_rod, 15),
        Building.constructor,
    ),
    Ingredients.screw:
    Recipe(
        RecipeIO(Ingredients.iron_rod, 10),
        RecipeIO(Ingredients.screw, 40),
        Building.constructor,
    ),
    Ingredients.reinforced_iron_plate:
    Recipe(
        RecipeIO(Ingredients.iron_plate, 30).add_item(Ingredients.screw, 60),
        RecipeIO(Ingredients.reinforced_iron_plate, 5),
        Building.assembler,
    ),
    Ingredients.rotor:
    Recipe(
        RecipeIO(Ingredients.iron_rod, 20).add_item(Ingredients.screw, 100),
        RecipeIO(Ingredients.rotor, 4),
        Building.assembler,
    ),
                                                                                                                                                                # Steel Ingot
    Ingredients.steel_ingot:
    Recipe(
        RecipeIO(Ingredients.iron_ore, 45).add_item(Ingredients.coal, 45),
        RecipeIO(Ingredients.steel_ingot, 45),
        Building.foundry,
    ),
    Ingredients.steel_beam:
    Recipe(
        RecipeIO(Ingredients.steel_ingot, 60),
        RecipeIO(Ingredients.steel_beam, 15),
        Building.constructor,
    ),
    Ingredients.steel_pipe:
    Recipe(
        RecipeIO(Ingredients.steel_ingot, 30),
        RecipeIO(Ingredients.steel_pipe, 20),
        Building.constructor,
    ),
    Ingredients.encased_industrial_beam:
    Recipe(
        RecipeIO(Ingredients.steel_beam, 24).add_item(Ingredients.concrete, 30),
        RecipeIO(Ingredients.encased_industrial_beam, 6),
        Building.assembler,
    ),
                                                                                                                                                                # Copper
    Ingredients.copper_ore:
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.copper_ore, 240),
        Building.miner_mk3,
    ),
    Ingredients.copper_ingot:
    Recipe(
        RecipeIO(Ingredients.copper_ore, 30),
        RecipeIO(Ingredients.copper_ingot, 30),
        Building.smelter,
    ),
    Ingredients.copper_powder:
    Recipe(
        RecipeIO(Ingredients.copper_ingot, 300),
        RecipeIO(Ingredients.copper_powder, 50),
        Building.constructor,
    ),
    Ingredients.copper_sheet:
    Recipe(
        RecipeIO(Ingredients.copper_ingot, 20),
        RecipeIO(Ingredients.copper_sheet, 10),
        Building.constructor,
    ),
    Ingredients.wire:
    Recipe(
        RecipeIO(Ingredients.copper_ingot, 15),
        RecipeIO(Ingredients.wire, 30),
        Building.constructor,
    ),
    Ingredients.cable:
    Recipe(
        RecipeIO(Ingredients.wire, 60),
        RecipeIO(Ingredients.cable, 30),
        Building.constructor,
    ),
                                                                                                                                                                # Raw Quartz
    Ingredients.raw_quartz:
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.raw_quartz, 240),
        Building.miner_mk3,
    ),
    Ingredients.quartz_crystal:
    Recipe(
        RecipeIO(Ingredients.raw_quartz, 37.5),
        RecipeIO(Ingredients.quartz_crystal, 22.5),
        Building.constructor,
    ),
    Ingredients.silica:
    Recipe(
        RecipeIO(Ingredients.raw_quartz, 22.5),
        RecipeIO(Ingredients.silica, 37.5),
        Building.constructor,
    ),
                                                                                                                                                                # Caterium
    Ingredients.caterium_ore:
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.caterium_ore, 240),
        Building.miner_mk3,
    ),
    Ingredients.caterium_ingot:
    Recipe(
        RecipeIO(Ingredients.caterium_ore, 45),
        RecipeIO(Ingredients.caterium_ingot, 15),
        Building.smelter,
    ),
    alternate(Ingredients.caterium_ingot):
    Recipe(
        RecipeIO(Ingredients.caterium_ore, 24).add_item(Liquid.water, 24),
        RecipeIO(Ingredients.caterium_ingot, 12),
        Building.smelter,
    ),
    Ingredients.quickwire:
    Recipe(
        RecipeIO(Ingredients.caterium_ingot, 12),
        RecipeIO(Ingredients.quickwire, 60),
        Building.constructor,
    ),
    alternate(Ingredients.quickwire):
    Recipe(
        RecipeIO(Ingredients.caterium_ingot, 7.5).add_item(Ingredients.copper_ingot, 37.5),
        RecipeIO(Ingredients.quickwire, 90),
        Building.constructor,
    ),
                                                                                                                                                                # Sulfur
    Ingredients.sulfur:
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.sulfur, 240),
        Building.miner_mk3,
    ),
    Ingredients.black_powder:
    Recipe(
        RecipeIO(Ingredients.coal, 15).add_item(Ingredients.sulfur, 15),
        RecipeIO(Ingredients.black_powder, 30),
        Building.assembler,
    ),
    Ingredients.compacted_coal:
    Recipe(
        RecipeIO(Ingredients.coal, 25).add_item(Ingredients.sulfur, 25),
        RecipeIO(Ingredients.compacted_coal, 25),
        Building.assembler,
    ),
                                                                                                                                                                # Liquid
    Liquid.water:
    Recipe(
        RecipeIO(),
        RecipeIO(Liquid.water, 120),
        Building.water_extractor,
    ),
    Liquid.crude_oil:
    Recipe(
        RecipeIO(),
        RecipeIO(Liquid.crude_oil, 120),
        Building.oil_extractor,
    ),
    Liquid.sulfuric_acid:
    Recipe(
        RecipeIO(Ingredients.sulfur, 50).add_item(Liquid.water, 50),
        RecipeIO(Liquid.sulfuric_acid, 50),
        Building.refinery,
    ),
                                                                                                                                                                # Intermediate material
    Ingredients.stator:
    Recipe(
        RecipeIO(Ingredients.steel_pipe, 15).add_item(Ingredients.wire, 40),
        RecipeIO(Ingredients.stator, 5),
        Building.assembler,
    ),
    Ingredients.ai_limiter:
    Recipe(
        RecipeIO(Ingredients.copper_sheet, 25).add_item(Ingredients.quickwire, 100),
        RecipeIO(Ingredients.ai_limiter, 5),
        Building.assembler,
    ),
    Ingredients.electromagnetic_control_rod:
    Recipe(
        RecipeIO(Ingredients.stator, 6).add_item(Ingredients.ai_limiter, 4),
        RecipeIO(Ingredients.electromagnetic_control_rod, 4),
        Building.assembler,
    ),

                                                                                                                                                                # Nuclear power
    Ingredients.uranium:
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.uranium, 240),
        Building.miner_mk3,
    ),
    Ingredients.encased_uranium_cell:
    Recipe(
        RecipeIO(Ingredients.uranium, 50).add_item(Ingredients.concrete, 15).add_item(Liquid.sulfuric_acid, 40),
        RecipeIO(Ingredients.encased_uranium_cell, 25).add_item(Liquid.sulfuric_acid, 10),
        Building.blender,
    ),
    alternate(Ingredients.encased_uranium_cell):
    Recipe(
        RecipeIO(Ingredients.uranium, 25).add_item(Ingredients.silica, 15).add_item(Ingredients.sulfur, 25).add_item(Ingredients.quickwire, 75),
        RecipeIO(Ingredients.encased_uranium_cell, 20),
        Building.manufacturer,
    ),
    Ingredients.uranium_fuel_rod:
    Recipe(
        RecipeIO(Ingredients.encased_uranium_cell, 20).add_item(Ingredients.encased_industrial_beam, 1.2).add_item(Ingredients.electromagnetic_control_rod, 2),
        RecipeIO(Ingredients.uranium_fuel_rod, 0.4),
        Building.manufacturer,
    ),
    Ingredients.uranium_waste:
    Recipe(
        RecipeIO(Ingredients.uranium_fuel_rod, 0.2).add_item(Liquid.water, 240),
        RecipeIO(Ingredients.uranium_waste, 10),
        Building.nuclear_power_plant,
    ),
}
