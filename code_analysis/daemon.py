"""
Socket-based daemon that holds indexes in memory.

This module is a backwards-compatibility wrapper. The actual implementation
has been modularized into the code_analysis.daemon package:
  - code_analysis.daemon.core: TLDRDaemon class
  - code_analysis.daemon.startup: start_daemon, stop_daemon, query_daemon
  - code_analysis.daemon.cached_queries: @salsa_query cached functions

For new code, import directly from code_analysis.daemon:
    from code_analysis.daemon import TLDRDaemon, start_daemon, query_daemon
"""

# Re-export everything for backwards compatibility
from code_analysis.daemon import (
    IDLE_TIMEOUT,
    TLDRDaemon,
    cached_architecture,
    cached_cfg,
    cached_context,
    cached_dead_code,
    cached_dfg,
    cached_extract,
    cached_importers,
    cached_imports,
    cached_search,
    cached_slice,
    cached_structure,
    cached_tree,
    main,
    query_daemon,
    start_daemon,
    stop_daemon,
)

__all__ = [
    "TLDRDaemon",
    "IDLE_TIMEOUT",
    "start_daemon",
    "stop_daemon",
    "query_daemon",
    "main",
    "cached_search",
    "cached_extract",
    "cached_dead_code",
    "cached_architecture",
    "cached_cfg",
    "cached_dfg",
    "cached_slice",
    "cached_tree",
    "cached_structure",
    "cached_context",
    "cached_imports",
    "cached_importers",
]

if __name__ == "__main__":
    main()
