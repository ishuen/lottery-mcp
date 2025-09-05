import logging
from typing import Any

from TaiwanLottery import TaiwanLotteryCrawler
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("lottery")
lottery = TaiwanLotteryCrawler()
logger = logging.getLogger(__name__)


@mcp.tool()
async def get_super_lotto_month(year: int, month: int) -> list[dict[str, Any]] | None:
    """Get lottery, super lotto 638 (威力彩), data in the specified month
        Args:
            year: target year, e.g. 2024
            month: target month, e.g. 5
    """
    try:
        response = lottery.super_lotto([str(year), str(month).zfill(2)])
        return response
    except Exception:
        logger.exception("Error occurred..", )
        return None


@mcp.tool()
async def get_lotto_649_month(year: int, month: int) -> list[dict[str, Any]] | None:
    """Get lottery, super lotto 649 (大樂透), data in the specified month
        Args:
            year: target year, e.g. 2024
            month: target month, e.g. 5
    """
    try:
        response = lottery.lotto649([str(year), str(month).zfill(2)])
        return response
    except Exception:
        logger.exception("Error occurred..", )
        return None

@mcp.tool()
async def get_daily_cash_month(year: int, month: int) -> list[dict[str, Any]] | None:
    """Get lottery, daily cash (今彩539), data in the specified month
        Args:
            year: target year, e.g. 2024
            month: target month, e.g. 5
    """
    try:
        response = lottery.daily_cash([str(year), str(month).zfill(2)])
        return response
    except Exception:
        logger.exception("Error occurred..", )
        return None

@mcp.tool()
async def get_lotto_4d_month(year: int, month: int) -> list[dict[str, Any]] | None:
    """Get lottery, lotto 4d (4星彩), data in the specified month
        Args:
            year: target year, e.g. 2024
            month: target month, e.g. 5
    """
    try:
        response = lottery.lotto4d([str(year), str(month).zfill(2)])
        return response
    except Exception:
        logger.exception("Error occurred..", )
        return None

if __name__ == "__main__":
    logger.info("Logger MCP server running..")
    mcp.run(transport='stdio')
