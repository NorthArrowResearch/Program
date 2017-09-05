---
layout: plugins
title: Plugin Repository
---

<a class="button" href="{{ site.baseurl }}/">Back to Riverscapes</a>

<p>Add <code class="highlighter-rouge">{{site.url}}/plugins.xml</code> as a plugin store in QGis to be able to download these plugins.</p>

<div id="pluginrepo" class="row small-up-1 medium-up-1 large-up-2">
<xsl:for-each select="/plugins/pyqgis_plugin">
<div class="column column-block">
  <ul class="plugin">
    <li class="title"><xsl:value-of select="@name" /> : <xsl:value-of select="@version" /></li>
    <li class="version">
      <span class="lbl">Version:</span>
      <span class="value"><xsl:value-of select="@version" /></span>
    </li>
    <li class="description"><xsl:value-of select="description" /></li>
    <li class="about"><xsl:value-of select="about" /></li>

    <li class="bullet-item"><span class="lbl">Author: </span><xsl:value-of select="author_name" /></li>
    <li class="bullet-item"><span class="lbl">Trusted: </span><xsl:value-of select="trusted" /></li>
    <li class="bullet-item"><span class="lbl">Experimental: </span><xsl:value-of select="experimental" /></li>
    <li class="bullet-item"><span class="lbl">Deprecated: </span><xsl:value-of select="deprecated" /></li>
    <li class="bullet-item"><span class="lbl">Minimum QGIS Version: </span><xsl:value-of select="qgis_minimum_version" /></li>

    <li class="bullet-item"><span class="lbl">Maximum QGIS Version: </span><xsl:value-of select="qgis_maximum_version" /></li>
    <li class="bullet-item"><span class="lbl">Tags: </span><xsl:value-of select="tags" /></li>

    <li class="cta-button">
      <xsl:element name="a">
         <xsl:attribute name="href"><xsl:value-of select="download_url" /></xsl:attribute>
         <xsl:attribute name="class">button</xsl:attribute>
          Download
      </xsl:element>      
    </li>
  </ul>
</div>
</xsl:for-each>
</div>

