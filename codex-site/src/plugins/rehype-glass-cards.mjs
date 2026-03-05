/**
 * Rehype plugin: wraps content sections between <hr> elements
 * in glass-card divs so each section becomes its own frosted panel
 * with background art visible between them.
 */
export default function rehypeGlassCards() {
  return (tree) => {
    const { children } = tree;
    if (!children || children.length === 0) return;

    const sections = [];
    let current = [];

    for (const node of children) {
      if (node.type === 'element' && node.tagName === 'hr') {
        // Push current section, start new one
        if (current.length > 0) {
          sections.push(current);
        }
        current = [];
      } else {
        current.push(node);
      }
    }
    // Push final section
    if (current.length > 0) {
      sections.push(current);
    }

    // Always wrap sections in glass cards
    tree.children = sections.map((sectionChildren) => ({
      type: 'element',
      tagName: 'div',
      properties: {
        className: ['glass-card', 'scroll-reveal'],
      },
      children: sectionChildren,
    }));
  };
}
